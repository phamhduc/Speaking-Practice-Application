import pickle
class Topic:
  def __init__(self):
    self.question = []
    self.answer = []
    self.topic ='' 

def Open_File():
  with open("AppData/topics.pkl", "rb") as f:
    Topics = pickle.load(f)
    return Topics
  
def Save_File(Topics):
  with open("AppData/topics.pkl", "wb") as f:
    pickle.dump(Topics, f)
    print("Save succes")


'''
T1 = Topic()

T1.answer = []
T1.question = []
T1.topic = ''
Topics = []
Topics.append(T1)

Save_File(Topics)

#TopicsT = Open_File()

#print(TopicsT[3].topic)

'''




