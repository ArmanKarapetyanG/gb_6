BOT_NAME = 'books_images'

SPIDER_MODULES = ['books_images.spiders']
NEWSPIDER_MODULE = 'books_images.spiders'


ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {'books_images.pipelines.BooksImagesPipeline': 1}

FILES_STORE = r'downloaded'


DOWNLOAD_DELAY = 1

