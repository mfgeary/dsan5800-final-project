import pandas as pd
import requests

BERT_API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"
SPELL_CHECK_API_URL = "https://api-inference.huggingface.co/models/oliverguhr/spelling-correction-english-base"

headers = {"Authorization": "Bearer API_KEY"}

def query(payload, API_URL=BERT_API_URL):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

homophones_list = [
    ['accessary', 'accessory'],
    ['ad', 'add'],
    ['ail', 'ale'],
    ['air', 'heir'],
    ['aisle', "I'll", 'isle'],
    ['all', 'awl'],
    ['allowed', 'aloud'],
    ['altar', 'alter'],
    ['arc', 'ark'],
    ['ant', 'aunt'],
    ['ate', 'eight'],
    ['auger', 'augur'],
    ['auk', 'orc'],
    ['aural', 'oral'],
    ['away', 'aweigh'],
    ['aw', 'awe'],
    ['ore', 'oar', 'or'],
    ['axel', 'axle'],
    ['aye', 'eye', 'I'],
    ['bail', 'bale'],
    ['bait', 'bate'],
    ['baize', 'bays'],
    ['bald', 'bawled'],
    ['ball', 'bawl'],
    ['band', 'banned'],
    ['bard', 'barred'],
    ['bare', 'bear'],
    ['bark', 'barque'],
    ['baron', 'barren'],
    ['base', 'bass'],
    ['based', 'baste'],
    ['bazaar', 'bizarre'],
    ['be', 'bee'],
    ['bay', 'bey'],
    ['beach', 'beech'],
    ['bean', 'been'],
    ['beat', 'beet'],
    ['beau', 'bow'],
    ['beer', 'bier'],
    ['bel', 'bell', 'belle'],
    ['berry', 'bury'],
    ['berth', 'birth'],
    ['bight', 'bite', 'byte'],
    ['billed', 'build'],
    ['bitten', 'bittern'],
    ['blew', 'blue'],
    ['bloc', 'block', 'bloque'],
    ['boar', 'bore'],
    ['board', 'bored'],
    ['boarder', 'border'],
    ['bold', 'bowled'],
    ['boos', 'booze'],
    ['born', 'borne'],
    ['bough', 'bow'],
    ['boy', 'buoy'],
    ['brae', 'bray'],
    ['braid', 'brayed'],
    ['braise', 'brays', 'braze'],
    ['brake', 'break'],
    ['bread', 'bred'],
    ['brews', 'bruise'],
    ['bridal', 'bridle'],
    ['broach', 'brooch'],
    ['bur', 'burr', 'brr'],
    ['but', 'butt'],
    ['buy', 'by', 'bye'],
    ['buyer', 'byre'],
    ['calendar', 'calender'],
    ['call', 'caul'],
    ['canvas', 'canvass'],
    ['cast', 'caste'],
    ['caster', 'castor'],
    ['caught', 'court'],
    ['caw', 'core', 'corps'],
    ['cede', 'seed'],
    ['ceiling', 'sealing'],
    ['cell', 'sell'],
    ['censer', 'censor', 'sensor'],
    ['cent', 'scent', 'sent'],
    ['cereal', 'serial'],
    ['cheap', 'cheep'],
    ['check', 'cheque'],
    ['choir', 'quire'],
    ['chord', 'cord'],
    ['cite', 'sight', 'site'],
    ['clack', 'claque'],
    ['clew', 'clue'],
    ['climb', 'clime'],
    ['close', 'cloze'],
    ['coal', 'kohl'],
    ['coarse', 'course'],
    ['coign', 'coin'],
    ['colonel', 'kernel'],
    ['complacent', 'complaisant'],
    ['complement', 'compliment'],
    ['coo', 'coup'],
    ['cops', 'copse'],
    ['council', 'counsel'],
    ['cousin', 'cozen'],
    ['creak', 'creek'],
    ['crews', 'cruise'],
    ['cue', 'kyu', 'queue'],
    ['curb', 'kerb'],
    ['currant', 'current'],
    ['cymbol', 'symbol'],
    ['dam', 'damn'],
    ['days', 'daze'],
    ['dear', 'deer'],
    ['descent', 'dissent'],
    ['desert', 'dessert'],
    ['deviser', 'divisor'],
    ['dew', 'due'],
    ['die', 'dye'],
    ['discreet', 'discrete'],
    ['doe', 'doh', 'dough'],
    ['done', 'dun'],
    ['douse', 'dowse'],
    ['draft', 'draught'],
    ['dual', 'duel'],
    ['earn', 'urn'],
    ['eery', 'eyrie'],
    ['ewe', 'yew', 'you'],
    ['faint', 'feint'],
    ['fah', 'far'],
    ['fair', 'fare'],
    ['fairy', 'ferry'],
    ['fate', 'fete'],
    ['farther', 'father'],
    ['faun', 'fawn'],
    ['faze', 'phase'],
    ['fay', 'fey'],
    ['feat', 'feet'],
    ['ferrule', 'ferule'],
    ['few', 'phew'],
    ['fie', 'phi'],
    ['file', 'phial'],
    ['find', 'fined'],
    ['fir', 'fur'],
    ['fizz', 'phiz'],
    ['flair', 'flare'],
    ['flaw', 'floor'],
    ['flea', 'flee'],
    ['flex', 'flecks'],
    ['flew', 'flu', 'flue'],
    ['floe', 'flow'],
    ['flour', 'flower'],
    ['for', 'fore', 'four'],
    ['foreword', 'forward'],
    ['fort', 'fought'],
    ['forth', 'fourth'],
    ['foul', 'fowl'],
    ['franc', 'frank'],
    ['freeze', 'frieze'],
    ['friar', 'fryer'],
    ['furs', 'furze'],
    ['gait', 'gate'],
    ['galipot', 'gallipot'],
    ['gamble', 'gambol'],
    ['gallop', 'galop'],
    ['gays', 'gaze'],
    ['genes', 'jeans'],
    ['gild', 'guild'],
    ['gilt', 'guilt'],
    ['giro', 'gyro'],
    ['gnaw', 'nor'],
    ['gneiss', 'nice'],
    ['gorilla', 'guerilla'],
    ['grate', 'great'],
    ['greave', 'grieve'],
    ['greys', 'graze'],
    ['grisly', 'grizzly'],
    ['groan', 'grown'],
    ['guessed', 'guest'],
    ['hail', 'hale'],
    ['hair', 'hare'],
    ['hall', 'haul'],
    ['hangar', 'hanger'],
    ['hart', 'heart'],
    ['haw', 'hoar', 'whore'],
    ['hay', 'hey'],
    ['heal', 'heel', "he'll"],
    ['here', 'hear'],
    ['heard', 'herd'],
    ["he'd", 'heed'],
    ['heroin', 'heroine'],
    ['hew', 'hue'],
    ['hi', 'high'],
    ['higher', 'hire'],
    ['him', 'hymn'],
    ['ho', 'hoe'],
    ['hoard', 'horde'],
    ['hoarse', 'horse'],
    ['holey', 'holy', 'wholly'],
    ['hour', 'our'],
    ['idle', 'idol'],
    ['in', 'inn'],
    ['indict', 'indite'],
    ["it's", 'its'],
    ['jewel', 'joule', 'juul'],
    ['key', 'quay'],
    ['knave', 'nave'],
    ['knead', 'need'],
    ['knew', 'new'],
    ['knight', 'night'],
    ['knit', 'nit'],
    ['knob', 'nob'],
    ['knock', 'nock'],
    ['knot', 'not'],
    ['know', 'no'],
    ['knows', 'nose'],
    ['laager', 'lager'],
    ['lac', 'lack'],
    ['lade', 'laid'],
    ['lain', 'lane'],
    ['lam', 'lamb'],
    ['laps', 'lapse'],
    ['larva', 'lava'],
    ['lase', 'laze'],
    ['law', 'lore'],
    ['lay', 'ley'],
    ['lea', 'lee'],
    ['leach', 'leech'],
    ['lead', 'led'],
    ['leak', 'leek'],
    ['lean', 'lien'],
    ['lessen', 'lesson'],
    ['levee', 'levy'],
    ['liar', 'lyre'],
    ['licence', 'license'],
    ['licker', 'liquor'],
    ['lie', 'lye'],
    ['lieu', 'loo'],
    ['links', 'lynx'],
    ['lo', 'low'],
    ['load', 'lode'],
    ['loan', 'lone'],
    ['locks', 'lox'],
    ['loop', 'loupe'],
    ['loot', 'lute'],
    ['made', 'maid'],
    ['mail', 'male'],
    ['main', 'mane'],
    ['maize', 'maze'],
    ['mall', 'maul'],
    ['manna', 'manner'],
    ['mantel', 'mantle'],
    ['mare', 'mayor'],
    ['mark', 'marque'],
    ['marshal', 'martial'],
    ['marten', 'martin'],
    ['mask', 'masque'],
    ['maw', 'more'],
    ['me', 'mi'],
    ['mean', 'mien'],
    ['meat', 'meet', 'mete'],
    ['medal', 'meddle'],
    ['metal', 'mettle'],
    ['meter', 'metre'],
    ['might', 'mite'],
    ['miner', 'minor', 'mynah'],
    ['mind', 'mined'],
    ['missed', 'mist'],
    ['moat', 'mote'],
    ['mode', 'mowed'],
    ['moor', 'more'],
    ['moose', 'mousse'],
    ['morning', 'mourning'],
    ['muscle', 'mussel'],
    ['naval', 'navel'],
    ['nay', 'neigh'],
    ['nigh', 'nye'],
    ['none', 'nun'],
    ['od', 'odd'],
    ['ode', 'owed'],
    ['oh', 'owe'],
    ['one', 'won'],
    ['packed', 'pact'],
    ['packs', 'pax'],
    ['pail', 'pale'],
    ['pain', 'pane'],
    ['pair', 'pare', 'pear'],
    ['palate', 'palette', 'pallet'],
    ['pascal', 'paschal'],
    ['paten', 'patten', 'pattern'],
    ['pause', 'paws', 'pores', 'pours'],
    ['peace', 'piece'],
    ['peak', 'peek', 'pique', 'peke'],
    ['pea', 'pee'],
    ['peal', 'peel'],
    ['pearl', 'purl'],
    ['pedal', 'peddle'],
    ['peer', 'pier'],
    ['pi', 'pie'],
    ['pica', 'pika'],
    ['place', 'plaice'],
    ['plain', 'plane'],
    ['pleas', 'please'],
    ['pole', 'poll'],
    ['plum', 'plumb'],
    ['poof', 'pouffe'],
    ['practice', 'practise'],
    ['praise', 'prays', 'preys'],
    ['principal', 'principle'],
    ['profit', 'prophet'],
    ['quarts', 'quartz'],
    ['quean', 'queen'],
    ['rain', 'reign', 'rein'],
    ['raise', 'rays', 'raze'],
    ['rap', 'wrap'],
    ['raw', 'roar'],
    ['read', 'reed'],
    ['read', 'red'],
    ['real', 'reel'],
    ['reek', 'wreak'],
    ['rest', 'wrest'],
    ['retch', 'wretch'],
    ['review', 'revue'],
    ['rheum', 'room'],
    ['right', 'rite', 'wright', 'write'],
    ['ring', 'wring'],
    ['road', 'rode'],
    ['roe', 'row'],
    ['role', 'roll'],
    ['roo', 'roux', 'rue'],
    ['rood', 'rude'],
    ['root', 'route'],
    ['rose', 'rows'],
    ['rota', 'rotor'],
    ['rote', 'wrote'],
    ['rough', 'ruff'],
    ['rouse', 'rows'],
    ['rung', 'wrung'],
    ['rye', 'wry'],
    ['saver', 'savour'],
    ['scull', 'skull'],
    ['spade', 'spayed'],
    ['sale', 'sail'],
    ['sane', 'seine'],
    ['satire', 'satyr'],
    ['sauce', 'source'],
    ['saw', 'soar', 'sore'],
    ['scene', 'seen'],
    ['sea', 'see'],
    ['seam', 'seem'],
    ['sear', 'seer', 'sere'],
    ['seas', 'sees', 'seize'],
    ['shake', 'sheikh'],
    ['sew', 'so', 'sow'],
    ['shear', 'sheer'],
    ['shoe', 'shoo'],
    ['sic', 'sick'],
    ['side', 'sighed'],
    ['sign', 'sine'],
    ['sink', 'synch'],
    ['slay', 'sleigh'],
    ['sloe', 'slow'],
    ['sole', 'soul'],
    ['some', 'sum'],
    ['son', 'sun'],
    ['sort', 'sought'],
    ['spa', 'spar'],
    ['staid', 'stayed'],
    ['stair', 'stare'],
    ['stake', 'steak'],
    ['stalk', 'stork'],
    ['stationary', 'stationery'],
    ['steal', 'steel'],
    ['stile', 'style'],
    ['storey', 'story'],
    ['straight', 'strait'],
    ['sweet', 'suite'],
    ['swat', 'swot'],
    ['tacks', 'tax'],
    ['tale', 'tail'],
    ['talk', 'torque'],
    ['tare', 'tear'],
    ['taught', 'taut', 'tort'],
    ['te', 'tea', 'tee', 't', 'ti'],
    ['team', 'teem'],
    ['tear', 'tier'],
    ['teas', 'tease'],
    ['terce', 'terse'],
    ['tern', 'turn'],
    ['there', 'their', "they're"],
    ['threw', 'through', 'thru'],
    ['throes', 'throws'],
    ['throne', 'thrown'],
    ['thyme', 'time'],
    ['tic', 'tick'],
    ['tide', 'tied'],
    ['tire', 'tyre'],
    ['to', 'too', 'two'],
    ['toad', 'toed', 'towed'],
    ['told', 'tolled'],
    ['tole', 'toll'],
    ['ton', 'tun'],
    ['tor', 'tore'],
    ['tough', 'tuff'],
    ['troop', 'troupe'],
    ['tuba', 'tuber'],
    ['vain', 'vane', 'vein'],
    ['vale', 'veil'],
    ['vial', 'vile'],
    ['vice', 'vise'],
    ['wade', 'weighed'],
    ['weak', 'week'],
    ['we', 'wee', 'whee'],
    ['way', 'weigh', 'whey'],
    ['wax', 'whacks'],
    ['wart', 'wort'],
    ['watt', 'what'],
    ['warn', 'worn'],
    ['ware', 'wear', 'where'],
    ['war', 'wore'],
    ['wall', 'waul'],
    ['waive', 'wave'],
    ['wait', 'weight'],
    ['wail', 'wale', 'whale'],
    ['wain', 'wane'],
    ["we'd", 'weed'],
    ['weal', "we'll", 'wheel'],
    ['wean', 'ween'],
    ['weather', 'whether'],
    ['weaver', 'weever'],
    ['weir', "we're"],
    ['were', 'whirr'],
    ['wet', 'whet'],
    ['wheald', 'wheeled'],
    ['which', 'witch'],
    ['whig', 'wig'],
    ['while', 'wile'],
    ['whine', 'wine'],
    ['whirl', 'whorl'],
    ['whirled', 'world'],
    ['whit', 'wit'],
    ['white', 'wight'],
    ["who's", 'whose'],
    ['woe', 'whoa'],
    ['wood', 'would'],
    ['yaw', 'yore', 'your', "you're"],
    ['yoke', 'yolk'],
    ["you'll", 'yule']
]

# Define the spelling correction function
def correct_spelling(input_text):
    output = query(payload={"inputs": input_text}, API_URL=SPELL_CHECK_API_URL)
    return output[0]["generated_text"]

def homophone_checker(input_string, homophones_list=homophones_list, score_threshold=0):
    # Final output sentence 
    total_sentence = input_string

    # Lowering the input string
    input_string = input_string.lower()
    input_string_list = input_string.split(" ")
    
    # Flatten homophones list
    all_homophones = [
        word for homophone_set in homophones_list for word in homophone_set
    ]

    # Find homophones in input string
    target_homophones = [(word, i) for i, word in enumerate(input_string_list) if list(set([word]).intersection(set(all_homophones)))]
    # print(target_homophones)

    # If there are no homophones in the sentence, return the NA dataframe
    if len(target_homophones) < 1:
        output_df = pd.DataFrame(
            {
                "sentence": input_string,
                "has_homophone": False,
                "is_error": None,
                "error_idx": None,
                "error": None,
                "correct_word": None,
                "correct_sentence": None,
            }, index=[0]
        )
        return output_df

    else:
        final_sentence, is_error, correct_word, error_idx, error = [], [], [], [], []


        for target_homophone_tuple in target_homophones:
            target_homophone = target_homophone_tuple[0]
            target_homophone_idx = target_homophone_tuple[1]

            input_string_list = input_string.split(" ")
            
            # Get all homophone options from homophones list
            homophone_options = [homophone for homophone in homophones_list if target_homophone in homophone]

            # Replace homophone with mask token
            input_string_list[target_homophone_idx] = "[MASK]"
            masked_string = ' '.join(input_string_list)

            payload = {"inputs": masked_string, "options": homophone_options, "top_k": 20}
            response = query(payload, API_URL=BERT_API_URL)

            if response:
                results = response
            else:
                # Handle error response
                final_sentence.append(input_string)
                is_error.append(False)
                correct_word.append(None)
                error_idx.append(None)
                error.append(None)
                continue

            # Token string dict
            token_string_dict = {}

            # Get top results and their score
            for result in results:
                try:
                    token_string_dict[result["token_str"]] = result["score"]
                except TypeError:
                    pass

            # Sort results
            sorted_results = sorted(token_string_dict.items(), key=lambda x: x[1], reverse=True)

            # Find top homophone in results
            homophone_results = [result for result in sorted_results if result[0] in homophone_options[0]]
            
            # If the top result is the target homophone, return the original sentence as it is correct
            try:
                top_result = homophone_results[0][0]
            except IndexError:
                final_sentence.append(input_string)
                is_error.append(False)
                correct_word.append(None)
                error_idx.append(None)
                error.append(None)
                continue

            if top_result == target_homophone:
                final_sentence.append(input_string)
                is_error.append(False)
                correct_word.append(None)
                error_idx.append(None)
                error.append(None)

            else:
                # If the top result is not the target homophone, check how many options it found
                # If multiple options:
                if len(homophone_results) > 1:

                    # Check the difference between the top two results
                    score_diff = homophone_results[0][1] - homophone_results[1][1]

                    # If the difference is greater than the threshold, return the top result
                    if score_diff > score_threshold:
                        error_idx.append(input_string.split(" ").index(target_homophone))
                        error.append(target_homophone)
                        final_sentence.append(input_string.replace(target_homophone, homophone_results[0][0]))
                        correct_word.append(homophone_results[0][0])
                        is_error.append(True)

                        total_sentence = total_sentence.replace(target_homophone, homophone_results[0][0])
                
                # If the difference is less than the threshold, return the original sentence
                else:
                    is_error.append(True)
                    error_idx.append(input_string.split(" ").index(target_homophone))
                    final_sentence.append(input_string.replace(target_homophone, homophone_results[0][0]))
                    correct_word.append(homophone_results[0][0])
                    error.append(target_homophone)

                    total_sentence = total_sentence.replace(target_homophone, homophone_results[0][0])

        # After obtaining the correct_sentence
        correct_sentence = total_sentence  # This is the sentence after homophone correction
        spelling_correct_sentence = correct_spelling(correct_sentence)  # Perform spelling correction
        print(spelling_correct_sentence)

        # Create output DataFrame with an additional column for spelling_correct_sentence
        output_df = pd.DataFrame(
            {
                "sentence": input_string,
                "has_homophone": True,
                "is_error": any(is_error),
                "error_idx": [[e for e in error_idx if e is not None]],
                "error": [[e for e in error if e is not None]],
                "correct_word": [[word for word in correct_word if word is not None]],
                "correct_sentence": correct_sentence,
                "spelling_correct_sentence": spelling_correct_sentence,  # New column
            }, index=[0]
        )

        return output_df
