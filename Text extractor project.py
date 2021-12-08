def iter_xth_word(x, filestream):
    """Iterates over xth word from each line of a file."""
    for line in filestream:
        try:
            yield line.split()[x-1]
        except IndexError:
            # ignore lines without a xth word
            continue

with open('news.txt', 'r') as file:
    # create the iterator using a generator comprehension
    iter_word_3 = iter_xth_word(7, file)
    # feed the iterator to the list function
    threes = list(iter_word_3)
    print(threes)
    print(*threes, sep = "\n") 
    
    with open('readme.txt', 'w') as f:
      for line in threes:
        f.write(line)
        f.write('\n')
    
        
    
    
    
    
    
    
    
    
    
    