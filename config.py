
ARCHS = ['i386', 'amd64']

SECTIONS = ('main', 'universe', 'multiverse', 'restricted')

DISTS = [
    'warty', 'hoary', 'breezy', 'dapper', 'edgy', 'feisty', 'gutsy', 'hardy',
    'intrepid', 'jaunty', 'karmic', 'lucid', 'maverick', 'natty', 'oneiric',
    'precise', 'quantal', 'raring', 'saucy', 'trusty', 'utopic', 'vivid',
    'wily', 'xenial', 'yakkety'
]

REPOS = {
    'warty': 'old',
    'hoary': 'old',
    'breezy': 'old',
    'dapper': 'old',
    'edgy': 'old',
    'feisty': 'old',
    'gutsy': 'old',
    'hardy': 'old',
    'intrepid': 'old',
    'jaunty': 'old',
    'karmic': 'old',
    'lucid': 'old',
    'maverick': 'old',
    'natty': 'old',
    'oneiric': 'old',
    'precise': 'current',
    'quantal': 'old',
    'raring': 'old',
    'saucy': 'old',
    'trusty': 'current',
    'utopic': 'old',
    'vivid': 'current',
    'wily': 'current',
    'xenial': 'current',
    'yakkety': 'current',
}

BASE_URLS = {
    'current': 'http://id.archive.ubuntu.com/ubuntu',
    'old': 'http://old-releases.ubuntu.com/ubuntu'
}

