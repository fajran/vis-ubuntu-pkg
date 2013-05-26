
ARCHS = ['i386', 'amd64']

SECTIONS = ('main', 'universe', 'multiverse', 'restricted')

DISTS = [
    'warty', 'hoary', 'breezy', 'dapper', 'edgy', 'feisty', 'gutsy', 'hardy',
    'intrepid', 'jaunty', 'karmic', 'lucid', 'maverick', 'natty', 'oneiric',
    'precise', 'quantal', 'raring'
]

REPOS = {
    'warty': 'old',
    'hoary': 'old',
    'breezy': 'old',
    'dapper': 'old',
    'edgy': 'old',
    'feisty': 'old',
    'gutsy': 'old',
    'hardy': 'current',
    'intrepid': 'old',
    'jaunty': 'old',
    'karmic': 'old',
    'lucid': 'current',
    'maverick': 'old',
    'natty': 'current',
    'oneiric': 'current',
    'precise': 'current',
    'quantal': 'current',
    'raring': 'current',
}

BASE_URLS = {
    'current': 'http://archive.ubuntu.com/ubuntu',
    'old': 'http://old-releases.ubuntu.com/ubuntu'
}

