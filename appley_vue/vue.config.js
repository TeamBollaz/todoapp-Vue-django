const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    publicPath: "http://127.0.0.1:8081",
    outputDir: "./dist/",

    chainWebpack: config => {
        config.optimization.splitChunks(false);

        config.plugin('BundleTracker').use(BundleTracker, [
            {
                filename: './webpack-stats.json'
            }
        ]);

        config.resolve.alias.set('__STATIC__', 'static');

        config.devServer
            .public('')
            .host('0.0.0.0')
            .port(8081)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({'Access-Control-Allow-Origin': ['\*']});
    }
};