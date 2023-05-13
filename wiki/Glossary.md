# Glossary of terms used

- **Inpainting**: latent text-to-image diffusion model  
  Select part of image and replace it with semantically generated context based on output prompt  
- **Outpainting**: technique to increase canvas and then use inpainting to fill missing parts  
- **Upscale**: run resulting image through additiona super-size ML model to increase resolution  
- **Textual inversion**: learn to generate specific concepts (objects, styles, persons)  
  by describing them using new words in the embedding space of a pre-trained model  
  creates embeddings assigned to one or more tokens from sample images  
- **Diffusers**: used to synthesize results by applying series of applications of denoising autoencoders  
- **Latent Diffusers**: its basically using diffusers in latent (abstract space) before generating pixel space  
  simply more efficient than running diffusers in pixel space  
- **Conditioning** or **Encoding**: text or image to semantic map  
- **Transformers**: generic ML model that add semantic understanding to trained area (text or image or audio or whatever)  
- **Checkpoint**": when training a model, save it as checkpoint every n epochs so training can be continued from there  
  checkpoint models can be further trained or used as-is  
- **Finetune model**: adds specific retraining using sample images to existing model  
  different than full retraining as it starts with existing checkpoint  
- **Hypernetwork**: finetune model and save as extension model instead of modifying original  
  this is basically an adaptive head - it takes information from late in the model but injects information from the prompt 'skipping' the rest of the model  
  similar to fine tuning the last 2 layers of a model but it gets much more signal from the prompt  
- **Dreambooth**: essentially model fine tuning, which changes the weights of the main model  
  differs from typical fine tuning in that in tries to keep from forgetting/overwriting adjacent concepts during the tuning  
- **Sampler**: which algorithm or lighweight ML model to use to add noise in each step before diffusion  
  different samplers are better at specific steps ranges and styles  
