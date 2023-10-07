import openai
from scholarly import scholarly
from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify
import json
app = Flask(__name__)
openai.api_key='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'

@app.route('/api/liveprompt',methods=['POST'])
def liveprompt():
    received_data=request.get_json()
    username=received_data['username']
    title=received_data['title']
    abstract=received_data['abstract']
    question="Title:'"+title+"'\n\nAbstract: "+abstract
    engineeredprompt=question+'\n'+"Make points which can be added to this abstract to make it more informative and useful for the reader.\n\n Response: MUST BE JSON(point1: 'point1', point2: 'point2', point3: 'point3', point4: 'point4', point5: 'point5', point6: 'point6', point7: 'point7', point8: 'point8', point9: 'point9', point10: 'point10')"
    questionreply=openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",
            temperature=0,

            messages=[
                    {"role": "system", "content": ""},
                    {"role": "user", "content": f"{engineeredprompt}"}
            ],       
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
    i=1
    points=[]
    while True:
            replytext=questionreply.choices[0].message.content
            points.append(json.loads(replytext)[f"point{i}"])
            print(points[i-1])
            if i==10:
                break
            i+=1
    return jsonify(points)
    # return questionreply.choices[0].message.content
@app.route('/api/tags/profile',methods=['POST'])
def profiletags():
    received_data=request.get_json()
    username=received_data['username']
    explainedinterests=received_data['explainedinterests']
    previousexperience=received_data['previousexperience']
    question="Interests: "+explainedinterests+"\n\nPrevious Experience: "+previousexperience
    engineeredprompt=question+'\n'+"Make EXACTLY 20 tags which can be added to this profile according to the specified interests and previous experiences\n\n Response: MUST BE JSON(tag1: 'tag1', tag2: 'tag2', tag3: 'tag3', tag4: 'tag4', tag5: 'tag5', tag6: 'tag6', tag7: 'tag7', tag8: 'tag8', tag9: 'tag9', tag10: 'tag10', tag11: 'tag11', tag12: 'tag12', tag13: 'tag13', tag14: 'tag14', tag15: 'tag15', tag16: 'tag16', tag17: 'tag17', tag18: 'tag18', tag19: 'tag19', tag20: 'tag20')"
    questionreply=openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",
            temperature=1,

            messages=[
                    {"role": "system", "content": "You're supposed to be creative while STRICTLY following instructions."},
                    {"role": "user", "content": f"{engineeredprompt}"}
            ],       
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
    i=1
    points=[]
    while True:
        replytext=questionreply.choices[0].message.content
        try:
            points.append(json.loads(replytext)[f"tag{i}"])
            print(points[i-1])
        except:
             pass
        if i==20:
            break
        i+=1

    return jsonify(points)

# @app.route('/api/tags/project',methods=['POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=='POST':
          print("Posted")
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)