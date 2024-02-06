const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
	context: path.resolve(__dirname, 'frontend'),
	entry: './src/main.js',
	output: {
		path: path.resolve(__dirname, 'frontend', 'dist'),
		publicPath: '/',
		filename: 'bundle.js',
	},
	resolve: {
		alias: {
			'@': path.resolve(__dirname, 'frontend', 'src'),
			'Assets': path.resolve(__dirname, 'frontend', 'src', 'assets'),
		},
		extensions: ['.js', '.vue'],
	},
	module: {
		rules: [
			{
				test: /\.vue$/,
				loader: 'vue-loader',
			},
			{
				test: /\.js$/,
				exclude: /node_modules/,
				use: {
					loader: 'babel-loader',
					options: {
						presets: ['@babel/preset-env'],
					},
				},
			},
			{
				test: /\.css$/,
				use: ['vue-style-loader', 'css-loader'],
			},
			{
				test: /\.s[ac]ss$/,
				use: ['vue-style-loader', 'css-loader', 'sass-loader'],
			},
			{
				test: /\.(png|jpe?g|gif|svg|webp)$/i,
				type: 'asset/resource',
				generator: {
					filename: 'assets/images/[name][ext]',
				},
			},
			{
				test: /\.(woff2?|eot|ttf|otf)$/i,
				type: 'asset/resource',
				generator: {
					filename: 'assets/fonts/[name][ext]',
				},
			},
		]
	},
	plugins: [
		new HtmlWebpackPlugin({
			template: path.resolve(__dirname, 'frontend', 'index.html'),
			inject: true,
		}),
		new VueLoaderPlugin(),
	],
};
