import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(PATH, "..", "conf", "project_template")

def import_user_module(module):
    """
        Imports a user module
    """
    
    try:
        return __import__(module, locals(), globals(), [])
    except ImportError:
        print "%s.py file not found!" % module
        sys.exit(1)  


def inspect_module(module, klass, get_first=False):    
    """
        Inspect a user module looking for [klass] type objects
    """
        
    objects = []
    for k,v in module.__dict__.iteritems():
        try:
            if issubclass(v, klass) and v is not klass:
                if get_first:
                    return v
                objects.append(v)
        except:
            pass
    if get_first:
        return None
    return objects


def command(store):
    """
        Decorator that adds a command to a dictionary
    """
            
    def wrap(f):            

        store[f.__name__] = f
    
        def decorated(*args, **kwargs):
            f(*args, **kwargs)
    
        return decorated
    return wrap


def generate_template(tm_name, project_name, output_dir):
    """
        Generates a project's file from a template 
    """

    with open(os.path.join(TEMPLATES_DIR, "%s.py") % tm_name, 'r') as f:
        
        template = f.read()
        data = template % { 'project_name' : project_name }
        
    with open(os.path.join(output_dir, "%s.py" % tm_name), 'w') as f:
        f.write(data)


def get_full_template_path(tm_name):
    """
        Returns the full template path 
    """
    
    return os.path.join(TEMPLATES_DIR, "%s.py" % tm_name)

