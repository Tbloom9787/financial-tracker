# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline

class StockPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):

        return "stocks/{id}.csv".format(
                   id=request.url.split("/")[6].lower()
               )