from Questionare import Questions
questionlist=[
    "\nWhich Cryptocurrency has a face of Dog in it ?  \n a.Dogecoin \n b.Bitcoin \n c.Solana \n d.Ethereum ",
    "\nWho is the Founder of Tesla ?  \n a.Bill Gates \n b.Elon Musk \n c.Mukesh Ambani \n d.Guido Van Rossum ",
    "\nWho is the Founder of Blue Origin ? \n a.Steve Jobs \n b.Elon Musk \n c.Jeff Bezos \n d.Larry Elison ",
    "\nWho is the Founder of Facebook ?\n a.Sam Martin \n b.Mark Zukerburg \n c.Mukesh Ambani \n d.Ratan Tata",
    "\nWho is the Founder of Realiance ?\n a.Mukesh Ambani \n b.Anil Ambani \n c.Akash Ambani \n d.Dhirubhai Ambani"
]
answerlist=["a","b","c","b","d"]
score=0
for i in range(0,5):
    print(questionlist[i])
    k=input("Enter your anwer:")
    sent = Questions(answerlist[i] ,k)
    if(sent.check()==1):
        score+=1
print("You Scored:",score,"/5")
