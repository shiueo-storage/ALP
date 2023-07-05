'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
print(Sentence) # this will print all elements in the list Sentence.
print(Sentence[1]) # this will print the word 'look' as the index starts with 0
Sentence.append("life") # this will append the word 'life' to the end index of the list
Sentence[4] = "sunny" # this will change the word to "sunny" which was in index 4
print(Sentence[4]) # it would be "sunny"
print(Sentence[0] + " " + Sentence[3]) # Always the
print(Sentence) # it will prints all the elements. the index 4 should be chnaged to sunny and at the end of the list, there sould be a word 'life'