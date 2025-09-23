3> The documents that dont have proper text strcture 

example - python code inside documents how to split with special characters 

4> Semantic meaning based splitting

splitting based on text meaning not on text length or structure 

It uses sliding window approach 

each sentence is taken and converted into vector embedding and cosine similarity is compared between 2 vectors . If similarity between 2 vectors are low then those 2 sentences context are different and splitting is performed there . 

threshold is set to find out value is decreasing or not 

each vector value is taken (ex 0.3,0.2,0.01), standard deviation is calculated of all numbers and  wherever similarity is more than standard deviation 