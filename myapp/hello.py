import fire

def hello(name="World"):
    return "Jinwoo says: Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
