from engine import Model

model = Model('decapoda-research/llama-65b-hf')

print(model)

with model.invoke('Hello world') as invoker:
    
    zzz = model.model.layers[0].output.copy()

output = model(device_map='server', max_new_tokens=1, return_dict_in_generate=True, output_scores=True)

breakpoint()