from invoke import Collection
from invoke.tasks import call

from invoke import task, run

@task
def clean(which=None):
    which = which or 'pyc'
    print("Cleaning {0}".format(which))

@task(pre=[call(clean, which='all')]) # or call(clean, 'all')
def build():
    print("Building")


ns = Collection(clean, build)
ns.configure({
    'run': {
        'echo': True,
        'pty': True,
    },
})
