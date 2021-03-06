from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/index.py")

@task
def build(ctx):
	ctx.run("python3 src/build.py")

@task 
def lint(ctx):
	ctx.run("pylint src")

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html")
