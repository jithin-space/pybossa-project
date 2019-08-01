import os
import json
def getTasks():
    cur = os.getcwd()+'/data';

    baseURL = 'http://localhost/project-docs/';

    files = [ f for f in os.listdir('data') if(os.path.isfile(os.path.join(cur,f)))]

    files = filter(lambda f: f.endswith(('.pdf','.PDF')), files);

    output = [{'url': baseURL+f,'id': i} for i,f in enumerate(files)];

    return output;

if __name__ == '__main__':
    file = open('tasks.json','w');
    tasks = getTasks();
    file.write(json.dumps(tasks));
    file.close();
