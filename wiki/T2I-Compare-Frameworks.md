# Generative Art Framework Comparisment

## Most Popular

### OpenAI Dall-E  

URL: <https://openai.com/dall-e-2/>  
Usage: SaaS (via native API and libraries), small base credits to start with, pay-to-play afterwards  
Training Size: 12B/6.5B/3.5B params  
Notes:  

- Commonly used is v2 which is better and smaller than v1  
  and its getting smaller and faster in each iteration  
- Best of available ones for human images  
- Style transfers or model modifers are charged extra  
- **Dall-E** is also licensed to 3rd parties as embedded engine:  
  Microsoft Designer, etc.  
- **Craiyon** as free smaller version (was "Dall-E Mini", but renamed due to copyright)  
  as original architects did not like commercial direction: <https://www.craiyon.com/>  
- **OpenAI Glide** is also from OpenAI, frequently ignored in favor of Dall-E, but not far result-wise  

### MidJourney  

URL: <https://midjourney.gitbook.io/docs/>  
Usage: SaaS (discord bot or web app) only, free to play with, pay-to-play for commercial usage  
Lead: David Holz
Notes:  

- Developed by research lab after lead sold his previous startup
- Quickest deccent looking results, but little tuning available  
- Results are often painting-like regardless of desired style  
- Often better 3D-effect than others  

### CompVis/Stability.AI/RunwayML Stable Diffusion  

URL: <https://stability.ai/>  
Training size: 1.4B params  
Usage: SaaS of offline usage, only fully open-source (**Creative ML OpenRAIL-M** license) to self-run  
Notes:  

- Originally research project by **CompVis**, continuing under **Stability.AI** entity but still open source  
- Training in partnership with **RunwayML**  
- Weights distributed via **HuggingFace** (only model with weights available)  
- Can be fiddly due to large number of modifiers and tunables, not great for faces out-of-the-box  
- Best results when using inpainting and adding of negative prompts  
- Version v2 removes styles from plenty authors and reduces tunables  
  Better photo-realistic results, but prompts require far more complexity to guide it  
- Official commerical product via **Stability.AI DreamStudio** <https://beta.dreamstudio.ai/dream>  

## Promising but not Available:

### nVidia eDiff-I  

URL: <https://deepimagination.cc/eDiff-I/>  
Usage: Not (yet) publicily available  
Training size: 9.1B params  
Note:  

- Looks very promising, especially with built-in style transfers  
- Somewhat different internal architecture with single-pass multi-encoders  

### Meta Make-a-Scene  

URL: <https://ai.facebook.com/blog/greater-creative-control-for-ai-image-generation/>  
Training size: 4B params  
Usage: Not publicily available  
Notes:  
- Future is likely meta internal tool until it becomes a filter for IG/FG or something  
- Can also generate videos: Make-a-Video  

### Google Imagen  

URL: <https://imagen.research.google/>  
Usage: Not publicily available  
Training size: 7.9B params  
Notes:  

- High-end research from **Google Brain**, not a commercial product  
- This is commonly used as a benchmark and reference point to see how good any other product is  
- Can also generate videos: <https://imagen.research.google/video/>  
- **Google DreamBooth** looks to separate algorithym to allow to  
  apply **Imagen** textual inversion techniques to other trained models: <https://dreambooth.github.io/>

### Google Parti  

URL: <https://parti.research.google/>  
Usage: Not publicily available  
Training size: 20B params  
Notes:

- Different architecture as it does not use diffusion at all
- True *SOTA*, but massively large (10x), better than anything

### Microsoft NUWA Infinity  

URL: <https://nuwa-infinity.microsoft.com/#/>  
Notes:

- Looks impressive, but no idea where its heading
