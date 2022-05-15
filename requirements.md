## Functional Requirements

1. Login -Steven
2. Logout -Steven
3. Create new account -Steven
4. Delete account -Inderpreet
5. Search bar -Inderpreet
6. Navbar -Christian
7. My wish list -Christian
8. Return policy -Joe
9. Discount promotions -Inderpreet
10. Stock Check -Steven
11. User Reviews -Joe
12. User profiles -Christian

## Non-functional Requirements

1. Dark Mode
2. Interactive User Interface with simple design -Christian
3. Will be able to work on multiple browsers
4. Low latency/Fast Performance

## Use Cases

1. Search bar
- **Pre-condition:** User is on website

- **Trigger:** User navigates to the search bar

- **Primary Sequence:**
  
  1. User inputs query
  2. User is able to narrow down search with year, artist, genre.
  3. User performs search function

- **Primary Postconditions:** User is presented with relevant search results.

- **Alternate Sequence:** 
  
  1. User inputs query
  2. User navigates off of the search bar without performing search function.

- **Alternate Sequence:** 
  
  1. User inputs query
  2. User performs search
  3. User is presented with no relevant search results.


2. My Shopping List
- **Pre-condition:** The user must be logged in.

- **Trigger:** User presses "My Shopping Cart" button

- **Primary Sequence:**
   1. Website retrieves list of items added to list by user.
   2. Website displays list of items sorted in lexicographic order.
   3. Website displays prices of all items next to each item's entry
   4. Website will sum up total price and quanity of all items and display it to the user
   
- **Primary Postconditions:**  User is presented with items and their respective prices in their cart.
 
- **Alterante Sequence:** 
 1. User is not logged in or does not have an account
 2. User is redirected to form to either log in or sign up
  
  
3. Promotions 
- **Pre-condition:** Item exists in store


-**Trigger:** All item's are peridoically sent through a rudimentary algothrim to determine if they will be selected for a set discount, or set by the poster.


-**Primary Sequence:** 
	1. Items that are selected by the algothrim will recieve a discount and length of discount determined by the algothrim. Item's
	selected by poster will have manually set discount.
	2. Items that are discounted will recieve special marking on their icon, and be displayed forefront on the webpage.
	

-**Primary Postcondition:** 
	Discounted are highlighted within the inventory section and promoted to users

4. My Wish list 

- **Precondition:** User is on a vinyl listing

- **Trigger:** User presses add to wish list button

- **Primary Sequence:**
	1. User presses the wish list button.
	2. Wish list button is highlighted

- **Primary Postcondition:** 
	Item(s) are stored within the wish list.

- **Alternate Sequence:** 
	1. User navigates to the Wish list. 
	2. User removes certain items from the Wish list.

- **Alternate Sequence:**
	1. User navigates to the wish list.
	2. User adds the wish list item(s) to the shopping cart.
	3. User proceeds to checkout.

5. Return Policy

- **Precondition:** User is on the website

- **Trigger:** User presses Return Policy button

- **Primary Sequence:**
	1. User presses the Return Policy button.
	2. User sees the Return Policies

- **Primary Postcondition:** 
	Return policies are shown.

- **Alternate Sequence:**
	1. User presses the Return Policy button.
	2. User sees the Return Policies.
	3. User navigates away from Return Policy

6. About
- **Precondition:** User is on the website

- **Trigger:** User presses About button

- **Primary Sequence:**
	1. User presses the About button.
	2. User sees the About details and description about the project/website

- **Primary Postcondition:** Description about the website is shown.

- **Alternate Sequence:**
	1. User presses the About button.
	2. User sees the website description and details.
	3. User navigates away from About.


