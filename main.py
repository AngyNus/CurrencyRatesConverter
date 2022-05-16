import Rates
import Gui

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    converter = Rates.Rates()

    print(converter.rates)
    print(converter.dollar_to_other(200, 'AED'))
    print(converter.other_to_dollar(200, 'AFN'))
    print(converter.other_to_dollar(100, 'ILS'))
    print(converter.dollar_to_other(100, 'ILS'))

    print(converter.exchange(100, 'ILS', 'THB'))
    #print(converter.exchange(200, 'ILS', 'USD'))
    #print(converter.exchange(1, 'ILS', 'USD'))

