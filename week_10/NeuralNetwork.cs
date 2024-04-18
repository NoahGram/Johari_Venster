using System;

public class NeuralNetwork
{
    private static Random rand = new Random();
    private double[,] weightsInputHidden = new double[4, 3];
    private double[,] weightsHiddenOutput = new double[3, 1];

    public NeuralNetwork()
    {
        // Initialize weights randomly
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 3; j++)
                weightsInputHidden[i, j] = rand.NextDouble();

        for (int i = 0; i < 3; i++)
            weightsHiddenOutput[i, 0] = rand.NextDouble();
    }

    public double[] FeedForward(double[] inputs)
    {
        double[] hiddenLayerOutputs = new double[3];
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 4; j++)
                hiddenLayerOutputs[i] += inputs[j] * weightsInputHidden[j, i];

        double output = 0;
        for (int i = 0; i < 3; i++)
            output += hiddenLayerOutputs[i] * weightsHiddenOutput[i, 0];

        return new double[] { output };
    }

    public void Train(double[][] inputs, double[] outputs, int numEpochs)
    {
        for (int epoch = 0; epoch < numEpochs; epoch++)
        {
            for (int i = 0; i < inputs.Length; i++)
            {
                double[] predictedOutputs = FeedForward(inputs[i]);
                double error = outputs[i] - predictedOutputs[0];

                // Adjust weights
                for (int j = 0; j < 4; j++)
                    for (int k = 0; k < 3; k++)
                        weightsInputHidden[j, k] += inputs[i][j] * error * 0.01;

                for (int j = 0; j < 3; j++)
                    weightsHiddenOutput[j, 0] += error * 0.01;
            }
        }
    }
}

public static void Main(string[] args)
{
    // Create a new neural network
    NeuralNetwork nn = new NeuralNetwork();

    // Define input and output data
    double[][] inputs = new double[][] {
        new double[] { 0, 0, 1, 1 },
        new double[] { 1, 1, 1, 0 },
        new double[] { 0, 1, 0, 1 },
        new double[] { 1, 0, 1, 0 },
        new double[] { 0, 1, 1, 0 }
    };
    double[] outputs = new double[] { 1, 1, 0, 0, 1 };

    // Train the neural network
    nn.Train(inputs, outputs, 10000);

    // Make a prediction
    double[] prediction = nn.FeedForward(new double[] { 0, 0, 1, 1 });

    // Print the prediction
    Console.WriteLine(prediction[0]);
}