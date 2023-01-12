# Adventuregame-in-python-tkinter

Introduction

	Find your queen game , in this game a knight have to find his queen that is hidden in any of given 10 rooms , a knight will be controlled by user , knight can move left , right , up and down  initial knight is at basement and queen is hidden in any room we are not aware of the room where she is hidden , we have have to find her. Now knight  has to fight the monsters for queen , in any room a ground or air monster can arrive , a ground monster can be killed by any weapon and air monster can only be killed by crossbow or pistol , a knight can only move to next room if he killed the monster , and a monster can only be killed by using a right weapon  if weapon is not right then knight will get killed by monster and you will loose game 

What Framework I used

I used Tkinter python plateform for making gui 

How you will win a game

User can win the game if knight reaches the queen , now queen is randomly placed in any room form 10 rooms , a knight needed to be move left , right ,up and down , and he has to fight the monsters that he will have in his way and by defeating all the monsters in his path  and  by reaching the room the knight will get his queen and he will win .

How knight will get a weapon 

In Every room randomly some items are placed , a user will be asked do he want to search items are not and he will search item in room for once and he will get any random item from the given list and then he will be prompt do he want to add that item in bag or not , if he want to add that item in bag then he can but before adding that item , user will check for bag space , total of bag space is 30 , and every item take space of 10 , this mean total of 3 useful items can be placed in bag .

Now if the bag is filled and you want to add new item in bag then , user will be asked do he want to remove last item in bag , and if he want to remove item and want to add new item then last element of bag will be pop out  and new item will be added instead of it .

Working of game


Game Start Menu

In this I have displayed 3 buttons Play , Help and exit , on clicking play game get start on clicking help a help menu get displayed and on clicking exit game get quit 

Play Option

On clicking play button a new geometry get displayed , which display 4 buttons name as move left , move right , move up and move down , 
if user click on move left knight get moved to left room and a she move to left room new screen prompt that show a new image that tell room is changes , initially as he enter the room he will be asked a question  do he want to search fro items in room , if he say yes then a random item get found in room , then he get asked do he want to add item into bag if he say yes then item get added into bad , on adding item into bag , we checked that is bag has space for item or not since bag can have maximum of 3 items , and every item take space of 10 so total of 30 space can be filled  , if user bag space is full then it will asked using message box that do he want to remove a item and add current item into bag , then if he say yes then new item get added into bag and previous item get removed from bag and space remain the same , after this we have place random ground or air monster in any of room , this mean on entering any room a monster can be arrive , if ground or air monster is found user will be displayed  that a ground monster or air monster is found then user have to use bag item to kill the monster , we asked  for user input the item  he will use to kill the monster and he will be displayed with bag items too that he can use , if the monster is ground monster then he can use any weapon  to kill the monster if the input weapon is correct then monster will get killed if the weapon is wrong then monster will kill knight and you will loose the game , if the monster is air then you have to use weapon that can kill air monster like crossbow and pistol ,  if the monster will killed by knight then he can move into next room to search the queen , queen is hidden in any random room if user reach the room successfully where queen is present then he will win the game and game will end 

How I perform this game

I used Tkinter  built in tools and widgets , for images I have  used Photoimage function in which I give the path of images I have used png images and all images size if width 900 and height of about 700 I have downloaded images from google and then I converted the images into png extension and have converted all the images to width 900 and height 600 using Canvas
For text I have created text labels using function Label in witch I set my text and other option 
For buttons I have used Button function of tkinter in which I set the text of buttons and other design 
For  text box I have used message box of tkinter.
