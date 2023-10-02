To build and run the docker image follow these steps:

1. Open the docker desktop
2. Open the terminal
3. Type in following command: docker build [Path to the project folder], then press Enter
4. After building an image type in the following command: docker images
5. Check and copy the ID of created image
6. Then type the following: docker run -p [any port that you prefer]:8001 [ID of an image]