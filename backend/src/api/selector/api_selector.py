from src.api.models import People
from src.api.serializer import PeopleSerializer

class ApiSelector:

    @staticmethod
    def getData():
        people=People.objects.all()[:300000]
        data=PeopleSerializer(instance=people,many=True).data
        results=[]
        for i in data:
            name=i.get('name')
            dics={
                "first_name":name.split(" ")[0],
                "last_name":name.split(" ")[1],
                "age":i.get('age'),
                "registered_at":i.get('registered_at')
            }
            results.append(dics)

        repeated_data={}
        for i in results:
            repeated_data={}
            first_name=i.get('first_name')
            last_name=i.get('last_name')
            for j in first_name:
                j=j.lower()
                if not repeated_data.get(j):
                    repeated_data[j]=1
                else:
                    repeated_data[j]+=1
                    
            i['repeated_first_name_freq']=repeated_data
            repeated_data={}

            for k in last_name:
                k=k.lower()
                if not repeated_data.get(k):
                    repeated_data[k]=1
                else:
                    repeated_data[k]+=1
                    
            i['repeated_last_name_freq']=repeated_data
            repeated_data={}




        return results