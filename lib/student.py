# class Student:
    
#     def hello(self):
#         print("Hey there! I'm so excited to learn stuff.")

#     def raise_hand(self):
#         print("Pick me!")

# class ChattyStudent(Student):

#     def says_hello(self):
#         return super().hello() + "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
#         # print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    

class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")



class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")


    def raise_hand(self):
        super().raise_hand()  
        for _ in range(9):
            super().raise_hand() 


    # def raise_hand(self):
    #     super().raise_hand()  
    #     for _ in range(9):
    #         super(ChattyStudent, self).raise_hand()





    # def raise_hand(self):
    #     super().raise_hand() 
    #     super().raise_hand() 
    #     super().raise_hand() 
    #     super().raise_hand() 
    #     super().raise_hand() 
    #     super().raise_hand() 
    #     super().raise_hand() 
    #     super().raise_hand() 
    #     super().raise_hand() 
    #     super().raise_hand() 
        







