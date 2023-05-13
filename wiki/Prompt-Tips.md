## Params

TL;DR: Tweak **steps**, **cfg scale** and **sampler** as results will vary depening on combination of all three  

- **Encoder**  
  Which text tokenizer to use, SD typically uses `CLiP`, but others can be substituted (`BERT`, `GPTx`, etc)  
- **Batch Size**  
  How many images to generate in parallel, limited by your VRAM  
- **Batch Count**  
  How many batches to run sequentially  
  So total number of images generated is batch size x batch count  
- **Seed**  
  Initializer for noise generator  
  Use same seed to have repeatable results, otherwise use random (-1)  
- **CFG Scale** (Classifer-Free-Guidance)  
  How close should diffusers follow prompt, 0 means none and 30 means exact  
  Best results are between 7 (creative) to 13 (realistic)  
  Higher CFG scale also removes details due to lower noise impact  
- **Width & Height**  
  SD 1.x is trained on 512x512 and SD 2.x is trained on 768x768  
  So typically don't change those and instead use upscalers if high resolution is needed  
  However, changing aspect ratio can change composition of image (e.g. portrait vs landscape results in close-up vs more wide angle results)  
- **Steps**  
  Directly impacts performance  
  How many iterative denoising steps to run, low number can lead to non-converged results (denoising is not complete)  
  Sweet-spot depends on chosen sampler, can be as low as 10 and as low as 100  
  Higher number of steps increases definition/precision/complexity of most important objects, but can completely remove secondary objects  
  At extreme steps values, all samplers converge since all noise is eventually removed  
- **Samplers**  
  Which algorithm or lighweight ML model to use to add noise in each step before diffusion  
  Different samplers are better at specific steps ranges and styles.  
  Different implementations of SD can prepackage different samplers  
  - Using different samplers may require different number of steps before noise is removed  
  - Eventually all samplers converge at high number of steps  
  - Some samplers may fit different styles better  

## Prompt Engineering

**Main groups**

- **Mediums**: best starting a prompt with it after specifying artist  
  Examples: *painting, photograph, drawing, sketch*
- **Flavors**: best left as separate token at the end of the prompt  
  Examples: *ray tracing, fine art, black and white, pixiv, artstation*
- **Movements**: best added to prompt with as keyword  
  Examples: *pop art, photorealism*  
- **Artists**: best starting a prompt with it  
  Examples: *greg rutkowski, artgerm, dc comics, picasso*  

**Modifiers**

- **Feel**: best near the end  
  Examples: *beautiful, sharp focus, 4k, hdr, high detailed, canon 5d*
- **Composition**: best at front, but only use if results don't fit  
  Examples: *1men, 1woman*

**Negative Prompt**

- Any keyword can be specified in a negative prompt as well
  Examples: *watermark*

**Advanced Prompt Modifiers**  

- Availability depends on implementation  
- Specify importance of specific words: E.g. using *"(word)"* means higher value while using *"[word]"* means lower value  
- Alternate between words: *"[word1|word2]"* if batch is 2, it will generate one image using *word1* and one image using *word2*  
- Force include multiple objects "AND"  

**Hints**

- Use either artists or movements  
  Do not use both as it will confuse model  
- Select medium that fits artist  
  It helps model a lot to know which medium to use when styling  
- Add action after subject  
  Examples: portrait, standing, sitting
- Moving things to the front of prompt may force styling, but limits choices  
  Example: *cartoon drawing of a woman as pixar* vs *pixar drawing of a woman*
- Use both subject and scene keywords:
  Example: *woman on a beach*

**Example**

> (composition) (artist) (medium) (subject) (action) (scene) (movement) (flavor) (feel)  
> 1woman greg rutkowski painting of a woman happy front portrait on a beach as photorealism, sharp focus, artstation
