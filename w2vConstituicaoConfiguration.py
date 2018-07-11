import yaml

class w2vConstituicaoConfiguration():

    #Configuration for open the config file
    CONFIGURATION_FILE_NAME = "config.yaml"
    FILE_LOAD_TYPE = "r"

    #Tags in the configuration file

    #PROJECT_CONFIGURATION
    PROJECT_CONFIGURATION_KEY = "PROJECT_CONFIGURATION"
    PROJECT_CONFIGURATION_VERBOSE_KEY = "verbose"
    PROJECT_CONFIGURATION_LIST_WORDS_VALIDATION_KEY = "list_words_validation"


    #SEED_CONFIGURATION
    SEED_CONFIGURATION_KEY = "SEED_CONFIGURATION"
    SEED_CONFIGURATION_TXT_FILE_KEY = "txt_file"


    @staticmethod
    def isVerbose():
        configuration = w2vConstituicaoConfiguration.__getConfigurationFile()
        configuration = configuration.get(w2vConstituicaoConfiguration.PROJECT_CONFIGURATION_KEY)

        return configuration.get(w2vConstituicaoConfiguration.PROJECT_CONFIGURATION_VERBOSE_KEY)

    @staticmethod
    def getListWordsValidation():
        configuration = w2vConstituicaoConfiguration.__getConfigurationFile()
        configuration = configuration.get(w2vConstituicaoConfiguration.PROJECT_CONFIGURATION_KEY)

        return configuration.get(w2vConstituicaoConfiguration.PROJECT_CONFIGURATION_LIST_WORDS_VALIDATION_KEY)

    @staticmethod
    def getFileName():
        configuration = w2vConstituicaoConfiguration.__getConfigurationFile()
        configuration = configuration.get(w2vConstituicaoConfiguration.SEED_CONFIGURATION_KEY)

        return configuration.get(w2vConstituicaoConfiguration.SEED_CONFIGURATION_TXT_FILE_KEY)


    @staticmethod
    def __getConfigurationFile():
        file = open(w2vConstituicaoConfiguration.CONFIGURATION_FILE_NAME, w2vConstituicaoConfiguration.FILE_LOAD_TYPE)

        with file as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as execution:
                print(execution)
