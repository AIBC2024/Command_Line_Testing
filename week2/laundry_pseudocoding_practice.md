# Laundry Pseudocode

```python
# Algorithm: Sorting Laundry


# Tasks:
We need to write pseudocode for the scenario of sorting and washing laundry

# Pattern recognition:
Sort basket 1 for white clothes
Sort basket 2 for red clothes
Sort basket 3 for delicates
Sort basket 4 for everything else

# Abstraction:
Ignore bedding
Ignire towels

# Sequence:
Loop for each of the color basket except the delicate one
1. Event 1: Put the basket of clothes in the machine.
2. Event 2: Apply the machine settings.
3. Event 3: Add laundry soap to the machine.
4. Event 4: Turn the machine on and wait until it's done.
5. Event 5: Remove the laundry and return it to the basket.

6. Event 6: After basket 1-3 are done, put special settings for the delicate setting 

```
###############################################


START LaundryProcess

// Initialize baskets
SET basket_white = EMPTY
SET basket_red = EMPTY
SET basket_delicates = EMPTY
SET basket_others = EMPTY

// Sorting Process
FOR EACH item IN dirty_laundry
    IF item is bedding OR item is towel THEN
        CONTINUE to next item
    END IF

    IF item is white THEN
        ADD item TO basket_white
    ELSE IF item is red THEN
        ADD item TO basket_red
    ELSE IF item is delicate THEN
        ADD item TO basket_delicates
    ELSE
        ADD item TO basket_others
    END IF
END FOR

// Washing Process
SET regular_baskets = [basket_white, basket_red, basket_others]

FOR EACH basket IN regular_baskets
    IF basket is NOT EMPTY THEN
        // Event 1
        PUT basket contents IN washing_machine
        
        // Event 2
        IF basket is basket_white THEN
            SET temperature TO "hot"
            SET cycle TO "normal"
        ELSE IF basket is basket_red THEN
            SET temperature TO "warm"
            SET cycle TO "normal"
        ELSE
            SET temperature TO "cold"
            SET cycle TO "normal"
        END IF
        
        // Event 3
        ADD laundry_soap TO washing_machine
        
        // Event 4
        START washing_machine
        WHILE washing_machine is running
            WAIT until cycle_complete
        END WHILE
        
        // Event 5
        REMOVE clothes FROM washing_machine
        PUT clothes IN basket
    END IF
END FOR

// Special handling for delicates (Event 6)
IF basket_delicates is NOT EMPTY THEN
    PUT basket_delicates IN washing_machine
    SET temperature TO "cold"
    SET cycle TO "delicate"
    ADD special_delicate_soap TO washing_machine
    
    START washing_machine
    WHILE washing_machine is running
        WAIT until cycle_complete
    END WHILE
    
    REMOVE clothes FROM washing_machine
    PUT clothes IN basket_delicates
END IF

END LaundryProcess