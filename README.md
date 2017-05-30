# Simple-Secret-Sharing-Script
A little python script that implements a (t,n)-threshold secret sharing scheme where t = n.

Shouldn't be that difficult to use.

Read more [here](https://en.wikipedia.org/wiki/Secret_sharing), specifically [here](https://en.wikipedia.org/wiki/Secret_sharing#t_.3D_n).



## Sample Walkthrough: 
```
$ ./secret.py 
Would you like to (S)plit a secret or (J)oin a secret? S

--- New Secret ---

File of secret to split: message.txt
Number of shares to create (>1): 3
Share filename prefix: message_share
Name of output directory: shares
$ ls shares/
message_share_0  message_share_1  message_share_2
$ ./secret.py 
Would you like to (S)plit a secret or (J)oin a secret? J

--- Join Secret ---

Directory name with shares: shares
Filename to output to secret to: secret_message.txt
```
