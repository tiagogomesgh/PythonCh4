### Tiago Gomes - 2375703
### COP1000 #1284

### Pseudocode
### PROMPT the user to enter a start, stop, and step value.
### STORE the Conversion factor of Short tons to Long tons, accurate to 9 digits.
### PRINT Column Headings, matching Alignments and Character Width.
### Use A FOR loop, to iterate through each interval, and CONVERT US Tons to Imperial Tons.



def main () :
### PROMPT the user to enter range of US Tons.
    start = int(input('Enter the start US tons value: '))
    stop = int(input('Enter the stop US tons value: '))
    step = int(input('Enter a step interval for US tons: '))

### Properly accounts for the final increment
    finalStop = stop + step
### Stores the proper, 9 digit conversion factor from Short Tons to Long Tons.    
    conversionFactor = 1.120000197

### The character width of 13 did not properly align like the desired output, So i used 19 :(
###. Allowing for proper alignment.    
### print(f"{'US Tons:^10}{'Imperial Tons':>13}")
    
    print(f"{'US Tons':^10}{'Imperial Tons':>19}")
    
### Iterates through each incrememnt and displays the US Tons + Imperial Tons.
    for num in range(start, finalStop, step):
        ### DISPLAY each value, accounting for character width and rounding to the 3rd decimal place.
          print(f'{num:^10}{num / conversionFactor:>13.3f}')

main ()
