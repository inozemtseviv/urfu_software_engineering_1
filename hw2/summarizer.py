from transformers import MBartTokenizer, MBartForConditionalGeneration


def summarize(text):
    model_name = 'IlyaGusev/mbart_ru_sum_gazeta'
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBartTokenizer.from_pretrained(model_name)

    input_ids = tokenizer(
        [text],
        max_length=600,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    return summary
