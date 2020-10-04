from aiohttp import web
import aiohttp_jinja2
import jinja2
import json

routes = web.RouteTableDef()

@web.middleware
async def redirect_php(request, handler):
  if request.path.endswith('.php'):
    return web.HTTPFound(request.path[:-4])
  response = await handler(request)
  return response

app = web.Application(middlewares=[redirect_php])

aiohttp_jinja2.setup(app,
  loader=jinja2.FileSystemLoader('templates'))

desc = '''Hi, I'm SushiPython, but you can call me Sushi. I like to code, as well as play video games. I know a few languages, including HTML, Python, and JS. Besides coding, I have always been interested in music, arts, and technology. I am currently learning backend JavaScript, as well as Java and MC Plugin Development. I have also been experimenting with Operating Systems such as Debian and ArchLinux.
I am a web developer, and nearly everything I code is available on a website. If not, it's probably a terminal. Most of my projects are open source and public on a site called replit, if you are ever curious on how I code any of my projects. You can send me an email at contact@sushipython.us, and for people who know what * means, you can send me an email at *@sushipython.us as well.
This site is made in HTML with Jinja2 templating and Python on the backend.'''

@routes.get('/')
@aiohttp_jinja2.template('index.html')
def index(request):
  return {'desc': desc}

@routes.get('/about')
@aiohttp_jinja2.template('about.html')
def about(request):
  return {'desc': desc}

@routes.get('/projects')
@aiohttp_jinja2.template('projects.html')
def projects(request):
  projectsDict = json.loads(open('site/projects.json', 'r').read())
  return {'pd': projectsDict}

app.add_routes(routes)
web.run_app(app)