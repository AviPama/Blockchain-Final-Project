# Project: Simple Blockchain-Based Product Tracking System

**Description:**

This project is a basic implementation of a blockchain-based system designed for tracking product movements in a supply chain. It demonstrates the fundamental concepts of blockchain technology, including the creation and linking of blocks, transaction recording, and a basic Proof of Work (PoW) mechanism. The system allows users to interact with the blockchain through a simple command-line interface.

**Key Components:**

**Block Class (block.py):** Defines the structure of each block in the blockchain, containing product movements, timestamps, and cryptographic hashes. It includes a basic PoW algorithm to secure the blocks.

**Blockchain Class (blockchain.py):** Manages the chain of blocks, ensuring data integrity and continuity of the blockchain. It handles the addition of new product movement records to the blockchain.

**Main Execution (main.py):** Provides a command-line interface for user interaction. It includes basic user authentication, allowing users to add product movements and view the history of any product in the blockchain.

**Features:**

**Product Movement Tracking:** Records and tracks the movements of products within a supply chain.

**Immutable Ledger:** Ensures that once a product movement is recorded, it cannot be altered or deleted.

**Proof of Work:** Implements a simple PoW mechanism for block validation, adding security to the blockchain.

**User Interaction:** Allows users to add new records and view the history of products through a user-friendly CLI.

**Basic User Authentication:** Manages user access, allowing only authenticated users to add information to the blockchain.
