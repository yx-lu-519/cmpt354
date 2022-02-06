# cmpt354
Database Systems

Application Requirements
Your application should either have a graphical user interface or a command line interface with a
hierarchical menu to support the following functions. Your submitted application should be run
directly on the workstations in CSIL without compiling by the user. For example, an .exe file or
an executable JAR file if you use Java for implementation. If you use Python, you can simply
submit a .py file that we can directly run. Note that once the program is running, it should allow
the tester to test all its functions and not terminate unless the tester manually closes the window or
console. The functions to be implemented are as follows:
Search Listings
1. This function allows the user to search for a suitable listing the satisfies certain criteria.
2. A user should be able to set the following filters as their search criteria: minimum and
maximum price, number of bedrooms, and start and end date.
3. After the search is complete, a list of search results must be shown to the user. The list
must include the following information for each listing: id, name, first 25 characters of
description, number of bedrooms, price. The results can be shown on the terminal or in a
GUI.
4. If the search result is empty, an appropriate message should be shown to the user.
Book Listing
1. A user must be able to select a listing from the results of the function Search Listings and
book it. This can be done by entering the listing’s id in a terminal or by clicking at a listing
in a GUI.
2. All the booking information should be recorded in the Booking table.
3. When a listing is booked, the Calendar table needs to be updated as well. This should
happen by the first trigger you wrote for assignment 4.
Write Review
1. A user should be able to write a review of a listing after his stay in that listing.
2. To write a review, a user must enter their name and the program should show all the
bookings of that user. Then the user can select one of their bookings and write a review of
that listing.
3. The following information should be asked from the user who wants to write a review:
user’s name, current date, review text.
4. The program should allow a review only if the given date is after the stay_to attribute of
the related booking record. You need to make sure that the triggers you implemented in
assignment 4 are working properly with your application program. If any error happened
in a trigger, your program should print the trigger’s error message and let the user know
that the review was not stored.
