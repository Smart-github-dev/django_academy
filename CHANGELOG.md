# Changelog

All notable changes to this project will be documented in this file.

### [0.10.2](https://github.com/fuchicorp/academy/compare/v0.10.1...v0.10.2) (2023-11-14)


### Bug Fixes

* Added beat and worker nodes and redis endpoint ([5c4afb8](https://github.com/fuchicorp/academy/commit/5c4afb8c4795eb3a96985a230da435eccce7ca50))
* Added helm charts with simple changes ([1acfbab](https://github.com/fuchicorp/academy/commit/1acfbabad14707780a1a5da531aac9f5d9d2df21))
* Added sending webhook messages to mentors channel ([a50c30c](https://github.com/fuchicorp/academy/commit/a50c30c72169ab7e802cc6a8d63f7b7fab2e1b57))
* Added sending webhook messages to mentors channel ([3d2f193](https://github.com/fuchicorp/academy/commit/3d2f19353cb257db199dd64b9857c435c24e8db5))
* Added the custom command to start the worker and the beat ([1484628](https://github.com/fuchicorp/academy/commit/1484628738be48522c0a30501bb577885a82c34a))
* Added volume to mount the academy folder and added videoFolders to the admin page ([31f0b94](https://github.com/fuchicorp/academy/commit/31f0b941bf8a1f7df9af9d0f7aedd3bd780dbbaa))
* Disabled the readiness probe ([711ecb2](https://github.com/fuchicorp/academy/commit/711ecb25ee82ce47c5fd2fa23b0afd070e6632be))
* Fixed the celery execution testing on stage ([a307739](https://github.com/fuchicorp/academy/commit/a307739ff788d86f668d1e17ec5e06a75e4b21d4))
* Implemented the celery and ready to test without envs ([531c701](https://github.com/fuchicorp/academy/commit/531c701499da72b663b0daa2e6b048148c68c0a4))
* Making sure the stage environment also paypal test ([8f22ab3](https://github.com/fuchicorp/academy/commit/8f22ab38d021b4cd74f39f456b03e35d89159783))
* Merged all the maps into one to manage properly ([c7ac9fc](https://github.com/fuchicorp/academy/commit/c7ac9fcfa656833933b0215e12ae8650490f549d))
* Removed the cancelation message from API ([cef0a11](https://github.com/fuchicorp/academy/commit/cef0a11a97f832d33d4e4398916fb709f036a0d9))
* Whitelisted the paypal endpoint and testing on the stage ([2978219](https://github.com/fuchicorp/academy/commit/297821978049724f1440c326bbf65041f75e9d5c))

### [0.10.1](https://github.com/fuchicorp/academy/compare/v0.10.0...v0.10.1) (2023-11-12)


### Bug Fixes

* has to be fixed asap to avoid the application to run in debug mode ([a0d4d17](https://github.com/fuchicorp/academy/commit/a0d4d177bd99f03c8601b81b63f203e8f4d93712))
* Stage and lower envs will be secured endpoint ([3f0f005](https://github.com/fuchicorp/academy/commit/3f0f005b66cd76f526f0f931abde1422eb725f04))

## [0.10.0](https://github.com/fuchicorp/academy/compare/v0.9.0...v0.10.0) (2023-11-12)


### Features

* Added new feature to get members from the academy ([c98a955](https://github.com/fuchicorp/academy/commit/c98a9557e512ddea7d6ff1033693c3bd1a1f7098))
* Implemented the SLACK notifications ([4b80e9c](https://github.com/fuchicorp/academy/commit/4b80e9c8c2093129b51651750f5f039e6f782433))
* Merged multiple PRs the source code needs to be cleaned up ([4c3d299](https://github.com/fuchicorp/academy/commit/4c3d299f0923d5c621f6e8b742e0aab05001e236))
* Merged multiple PRs the source code needs to be cleaned up ([aecabd9](https://github.com/fuchicorp/academy/commit/aecabd915fcb2b14a25386917c05d86fb26721c7))
* Now we can query from API list of members ([9e13df1](https://github.com/fuchicorp/academy/commit/9e13df17976370534f918f11d30a085708809a57))


### Bug Fixes

* Removed the markdown and upgraded the terraform version ([cd09b96](https://github.com/fuchicorp/academy/commit/cd09b96bfcf3ecdcaef3393254990f884974cfda))

## [0.9.0](https://github.com/fuchicorp/academy/compare/v0.8.1...v0.9.0) (2023-11-12)


### Features

* Merged multiple PRs the source code needs to be cleaned up ([#356](https://github.com/fuchicorp/academy/issues/356)) ([42f82f5](https://github.com/fuchicorp/academy/commit/42f82f541c1b1b696072c94b8a00849cd6540747))


### Bug Fixes

* congigured pre commit and added pipelines ([a17539a](https://github.com/fuchicorp/academy/commit/a17539a5039b75c44cbf76bda3b43eb5c31b1b68))
* Created custom script to update the password ([de5717a](https://github.com/fuchicorp/academy/commit/de5717a4becc152f49ab8d9cffc51585dfc5f190))
* Fixed problem with yaml syntax ([417f7a2](https://github.com/fuchicorp/academy/commit/417f7a28b4646b083b6657bb38afc8ee2be54bfb))
* Reconstructed the helm chart and terrform deployment ([ce5138f](https://github.com/fuchicorp/academy/commit/ce5138f0de8e1d7d3452848c3b0446ae9ce5dc23))
* Updated the semantic relase versioning pipeline ([eb95e30](https://github.com/fuchicorp/academy/commit/eb95e301caa39285c644949c2f25bf4cd1cd4d0f))
* Updated the tickets ([a501162](https://github.com/fuchicorp/academy/commit/a501162897ada13298a068697a4c6a066881e5d9))
* Upgrading the terraform version for academy ([b50ed9e](https://github.com/fuchicorp/academy/commit/b50ed9ed47e517ce4da55ef61103e8e6b7669f51))

### [0.8.1](https://github.com/fuchicorp/academy/compare/v0.8.0...v0.8.1) (2023-10-04)


### Bug Fixes

* Pre commit and commit message script fixed ([140993e](https://github.com/fuchicorp/academy/commit/140993e2819bd2e00f7abb91c833a334140f5a66))

## [0.8.0](https://github.com/fuchicorp/academy/compare/v0.7.0...v0.8.0) (2023-10-04)


### Features

* Created source code for AI chatting ([05d8465](https://github.com/fuchicorp/academy/commit/05d8465b235e614c2da268efe338cff886957525))
* Implemented the AI to academy ([76a8ba1](https://github.com/fuchicorp/academy/commit/76a8ba13dae6d6870a1d5deab6c05a56bd347cd7))


### Bug Fixes

* Letting people to see what kind of videos do we have ([a0f7a88](https://github.com/fuchicorp/academy/commit/a0f7a88b61fc6c8d217de2de174cb3b4aa992034))
* Loading most up to date videos ([83ed7db](https://github.com/fuchicorp/academy/commit/83ed7db04a495bae80f5b4646a8bf9e3655b144d))

## [0.7.0](https://github.com/fuchicorp/academy/compare/v0.6.29...v0.7.0) (2023-06-27)


### Features

* Added the fordbidden page ([118bdc8](https://github.com/fuchicorp/academy/commit/118bdc8e136ec8fbf1d3b6f4fd1267d523047402))
* Implement semantic release versioning for all repos ([#352](https://github.com/fuchicorp/academy/issues/352)) ([2446f54](https://github.com/fuchicorp/academy/commit/2446f54910478c350103c92598aadf1abc3a6dc0))
* Implemented the 403 page for academy [#351](https://github.com/fuchicorp/academy/issues/351) ([362be14](https://github.com/fuchicorp/academy/commit/362be14e6ba965449fb48b26fff95d11b9d66f88))
* Updated the endpoints correctly ([c541bc0](https://github.com/fuchicorp/academy/commit/c541bc0ac7a81dc2895941de040157dd1a37f15a))
