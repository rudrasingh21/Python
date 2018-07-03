
# coding: utf-8

# In[1]:


item1="bread"


# In[2]:


item2="pasta"


# In[3]:


item3="fruits"


# In[4]:


items=["bread","pasta","fruits","veggies"]


# In[5]:


items


# In[6]:


items[0]


# In[7]:


items[2]


# In[8]:


item[0]='chips'


# In[9]:


items[0]='chips'


# In[10]:


items


# In[ ]:


# In Above , it replaced item of index 0 with chips


# In[11]:


items[0:2]


# In[ ]:


# append --> will add entry in your list


# In[12]:


items.append('Butter')


# In[13]:


items


# In[ ]:


# New Example


# In[36]:


list1 = [1, 2, 3, 4]


# In[40]:


list2 = [6]


# In[38]:


list1.append(5)


# In[39]:


list1


# In[41]:


list1.append(list2)


# In[42]:


list1


# In[43]:


# To overcome above issue , we have extend


# In[45]:


list1.extend(list2)


# In[46]:


list1


# In[52]:


mylist = ['a','b','c','d']
mylist


# In[48]:


lang = 'java'
lang


# In[53]:


mylist.append(lang)
mylist


# In[54]:


mylist = ['a','b','c','d']
mylist


# In[55]:


mylist.extend(lang)


# In[56]:


mylist


# In[59]:


lst = ['java','c','php']
lst


# In[60]:


t = ['Python','sql','plsql']
t


# In[61]:


lst.append(t)
lst


# In[62]:


lst = ['java','c','php']
lst


# In[63]:


lst.extend(t)


# In[64]:


lst


# In[14]:


# insert --> will add entry ar desired location


# In[16]:


items.insert(0,'Lays')


# In[17]:


items


# In[18]:


# Join


# In[19]:


food = ["bread","pasta","fruits"]
bathroom = ["shampoo","soap"]


# In[20]:


food


# In[21]:


bathroom


# In[22]:


shopping = food + bathroom


# In[23]:


shopping


# In[24]:


# Length


# In[25]:


len(shopping)


# In[27]:


'bread' in shopping


# In[28]:


'soap' in shopping


# In[29]:


'pizza' in shopping

OTHER Examples:-
    
    list.pop(1)                  ## removes
    
    list.remove('curly')         ## search and remove that element
    
    list = ['larry', 'curly', 'moe']
    
    list.append('shemp')         ## append elem at end
    
    list.insert(0, 'xxx')        ## insert elem at index 0
    
    list.extend(['yyy', 'zzz'])  ## add list of elems at end