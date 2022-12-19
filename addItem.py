def addItem():
    recInfoList=['Record number','Item name','Item number','Category','Quantity','Weight','Recipient','Final destination','Delivery status']
    newItemList=[0]*len(recInfoList)
    index=0
    while index<len(recInfoList):
        newItemList[index]=input('Enter '+recInfoList[index]+':')
        index+=1
    return newItemList


        





