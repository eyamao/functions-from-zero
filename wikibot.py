from mylib.bot import scrape
import click

@click.command()
@click.option('--name', prompt="Wikipedia page to scrape", help='Web page to scrape')
@click.option('--length', default=1, prompt='Length of the output', help='Length of the requested output')
def cli(name='Microsoft',length=1):
    result = scrape(name, length=length)
    click.echo(click.style(f"{result}:", fg="white", bg="blue"))

if __name__ == '__main__':
    cli()



