from invoke import task

@task 
def foo(ctx):
	print("bar")

@task
def start(ctx):
	ctx.run("python3 src/index.py")

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest")

