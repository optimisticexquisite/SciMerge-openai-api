import openai
from flask import Flask, render_template, request, redirect, url_for, session,jsonify
import json
app = Flask(__name__)
openai.api_key='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'
question="Title:'Working with virtual assistance for blind people\n\nAbstract: The aim of this project is to develop a virtual assistance for blind people so that they can use the software communicate seamlessly with their other different senses."
engineeredprompt=question+'\n'+"Make points which can be added to this abstract to make it more informative and useful for the reader.\n\n Response: JSON(point1: 'point1', point2: 'point2', point3: 'point3', point4: 'point4', point5: 'point5', point6: 'point6', point7: 'point7', point8: 'point8', point9: 'point9', point10: 'point10')"
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