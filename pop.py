from prolog.CLI.terminal import CLI
from prolog.Parser.tokenizer import Tokenizer

def main():
    cli = CLI()
    while True:
        text = cli.prompt()
        tokenizer = Tokenizer(text)
        flag = True
        while flag:
           # token, flag = tokenizer.tokenize()
            cli._console.print(f"{token}\n")

if __name__=="__main__":
    main()


