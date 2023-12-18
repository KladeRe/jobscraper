# Base on offical Node.js Alpine image
FROM node:alpine

# Expose the listening port
EXPOSE 3000

# Set working directory
WORKDIR /react


COPY *.json ./

# Install PM2 globally
RUN npm install 


# Copy all files
COPY . .

RUN npm run build

# Run npm start script with PM2 when container starts
CMD ["npm", "start" ]