import sys

def getanswer(news):
    my_file = open("test_news_value.txt", "w")
    my_file.write(news)
    my_file.close()

    import test_model_detection_fake_news


    return test_model_detection_fake_news.answer

if "test_model_detection_fake_news" in sys.modules:
        del sys.modules["test_model_detection_fake_news"]
