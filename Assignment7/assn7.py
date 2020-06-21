import sys
import pyodbc
conn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_yla519;pwd=YdAaeh46M36g4Rqd')

while True:
    func=input("Enter 1 to Search Listings, 2 to Book Listing, 3 to Write Review, 4 to quit: ")
    if func=='1':
        mycursor=conn.cursor()
        minPrice=float(input("Enter minimum price: "))
        maxPrice=float(input("Enter maximum price: "))
        numBedr=int(input("Enter number of bedrooms: "))
        startDate=input("Enter start date 'MM/DD/YYYY': ")
        endDate=input("Enter end date 'MM/DD/YYYY': ")
        searchSQL=('SELECT A.id,A.name,A.description,A.number_of_bedrooms,T.sum FROM ((SELECT Listings.id,Listings.number_of_bedrooms,Listings.name,Listings.description from Listings where Listings.number_of_bedrooms = ?)A JOIN (select C.Listing_id,C.available,SUM(C.price)sum from(select* from Calendar where Calendar.price>=? and Calendar.price<=? and Calendar.date>=? and Calendar.date<=?)C group by C.listing_id,C.available having COUNT(C.listing_id) = SUM(CAST(C.available AS INT )) AND  COUNT(C.listing_id) = DATEDIFF(day,?,?)+1)T ON(A.id = T.listing_id))')
        values=[numBedr,minPrice,maxPrice,startDate,endDate,startDate,endDate]
        mycursor.execute(searchSQL,values)     
        row=mycursor.fetchone()
        if not row:
            print("No result. Back to menu.\n")
        while row:
            print("ID: "+ str(row[0]))
            print("Name: "+str(row[1]))
            tempdes=row[2]
            print("First 25 characters of description: "+tempdes[0:25])
            print("Number of bedrooms: "+str(row[3]))
            print("Total Price: "+str(row[4]))
            print("\n")
            row=mycursor.fetchone()
    elif func=='2':
        mycursor=conn.cursor()
        id=int(input("Enter booking ID: "))
        SQL1=('SELECT * FROM Bookings WHERE id=?')
        value1=[id]
        mycursor.execute(SQL1,value1)     
        row1=mycursor.fetchone()
        if row1:
            print("Already exist review. Insert failed. Back to menu.\n")
            continue
        l_id=int(input("Enter listing_id you want to book: "))
        name=input("Enter name: ")
        startDate=input("Enter start date 'MM/DD/YYYY': ")
        endDate=input("Enter end date 'MM/DD/YYYY': ")
        numGuest=int(input("Enter number of guests: "))
        SQL2=('INSERT INTO Bookings VALUES (?,?,?,?,?,?)')
        value2=[id,l_id,name,startDate,endDate,numGuest]
        mycursor.execute(SQL2,value2)
        conn.commit()
        SQL3=('SELECT * FROM Bookings WHERE id=? AND listing_id=? AND guest_name=? AND stay_from=? AND number_of_guests=?')
        mycursor.execute(SQL3,value2)
        row2=mycursor.fetchone()
        if row2:
            print("Success.\n")
        else:
            print("Fail.\n")
    elif func=='3':
#        assignment4 trigger
#        create trigger tr2_Review_insert on Reviews
#        after insert
#        as if not exists(select *
#        					from inserted i join Bookings b 
#        						on i.guest_name=b.guest_name and i.listing_id=b.listing_id 
#        					where GETDATE()>=stay_from)
#        --cannot submit a review before the end of their Booking of that List
#        begin
#        	rollback transaction
#        end
        mycursor=conn.cursor()
        name=input("Enter name to check your booking Info: ")
        SQL1=('SELECT b.id,b.guest_name,b.listing_id FROM Bookings b WHERE guest_name=?')
        value1=[name]
        mycursor.execute(SQL1,value1)     
        row1=mycursor.fetchone()
        if not row1:
            print("No result. Back to menu.\n")
            continue
        while row1:
            print("ID: "+ str(row1[0]))
            print("Guest_name: "+str(row1[1]))
            print("Listing_id: "+str(row1[2]))
            print("\n")
            row1=mycursor.fetchone()
#       Reviews (id,listing_id,comments,guest_name)
        Rid=int(input("Enter id of your review: "))
        Lid=int(input("Enter listing_id you want to comment: "))
        Rname=input("Enter name before write a review: ")
        text=input("Enter your review: ")
        SQL2=('select * from Reviews where id=?')
        value2=[Rid]
        mycursor.execute(SQL2,value2)
        row2=mycursor.fetchone()
        if row2:
            print("Already exists this ID. Insert fail. Back to menu.")
            continue
        SQL3=('INSERT INTO Reviews VALUES (?,?,?,?)')
        value3=[Rid,Lid,text,Rname]
        mycursor.execute(SQL3,value3)
        conn.commit()
        SQL4=('select * from Reviews where id=? and guest_name=?')
        value4=[Rid,Rname]
        mycursor.execute(SQL4,value4)
        row4=mycursor.fetchone()
        if row4:
            print("Success.\n")
        else:
            print("Fail.\n")
    elif func=='4':
        conn.close()
        sys.exit(0)