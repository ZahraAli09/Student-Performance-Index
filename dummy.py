from fastapi import FastAPI, Request
import pickle

app=FastAPI()

file=open('performance.pkl', 'rb')
model=pickle.load(file)

#creating an API
@app.get('/')
def home():
    return {'message': 'Hello Everyone'}
@app.post('/path1')
async def data(request: Request):
    if request.method=='POST':
        data=await request.json()
        return {"message": data}
@app.post('/path2')
async def student_performance(request:Request):
    if request.method == 'POST':
        data = await request.json()
        print(data)
        hours_studied = int(data['hours_studied'])
        previous_score = int(data['previous_scores'])
        hours_sleep = int(data['sleep_hours'])
        sample_paper = int(data['sample_paper'])
        activity=data['activity']

        if activity=='yes':
            yes=1
            no=0

        else:
            yes=0
            no=1   

        x = model.predict([[hours_studied, 
                            previous_score, 
                            hours_sleep,
                            sample_paper,
                            no,
                            yes]])
        
        # print(int(x), type(x))
        return {"Performance Index":int(x)}   