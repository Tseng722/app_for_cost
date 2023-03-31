import sys                               #class Record:
#from pyrecord import Record   
#from pyrecord import Records   
global category ,records
class Category:
    """Maintain the category list and provide some methods."""
    def __init__(self,y):
        self.category=['expense',['food',['snack','meal','drink'],'transportation',['train','bus','car']],'income',['salary','bonus']]
        self.records=y
        self.cc=[]
        self.ll=[]
    def view(self,k,level=0):
        """view all categories"""
        if k==None:
            return
        if type(k) in {list,tuple}:
            for item in k:
                self.view(item,level+1)
        else:
            self.cc.insert(0,f'{" "*4*level}-{k}')

        return self.cc

    def find_cate(self,category_input,category):
        """find record under specificed category"""
        def find_cate_gen(category_input,category,found=False):
            if type(category)==list:
                for i,v in enumerate(category):
                    yield from find_cate_gen(category_input,v,found=False)
                    if v==category_input and i + 1 < len(category) and type(category[i+1])==list :
                        found=True
                        for qq in category[i+1]:
                            if type(qq)!=list:
                                yield from find_cate_gen(qq,qq,found=True)
                            else:
                                for ww in qq:
                                    yield from find_cate_gen(qq,ww,found=True)
            else:
                if category==category_input or found==True:
                    yield category
        qq=find_cate_gen(category_input,category)
        category_list=[i for i in qq]
        if category_list==[]:
            ll=filter(lambda i: category_input in i[0],self.records)
        else:
            ll=filter(lambda i: i[1] in category_list,self.records)
        self.ll=list(ll)

        #print(f"Here's your expense and income records under category '{category_input}':")
        #print('   Date     Category  Description    Amount')
        #print('__________  ________  ___________    ______')
        #b=0
        #for i in self.ll:
        #    print('%5s %8s %10s %12d' %(i[0],i[1],i[2],i[3]))
        #    b=b+i[3]
        #print('___________________________________________')
        #print(f'The total amount above is {b}')

    def category_valid(self,item,cateegories):
        return False if item not in ['expense','food','snack','meal','drink','transportation','train','bus','car','income','salary','bonus'] else True

