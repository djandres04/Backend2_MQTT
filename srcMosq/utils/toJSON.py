def to_json(topic, value, id):
    if id is None:
        return   {'topic':topic,
                'value':str(value)}  
    else:
        return  {'topic':topic,
                'id':str(id),
                'status':str(value)}