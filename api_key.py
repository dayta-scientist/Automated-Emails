import os


def main():
    api_key = os.environ.get('NewsAPI_api_key')
    return api_key


if __name__=='__main__':
    main()