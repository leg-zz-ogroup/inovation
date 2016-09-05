var gulp = require('gulp');
var gutil = require('gulp-util');
var bower = require('bower');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
//var uglify = require('gulp-uglify');
var minifyCss = require('gulp-minify-css');
var rename = require('gulp-rename');
//var sh = require('shelljs');

var paths = {
    sass: ['static/scss/**/*.scss'],
    scripts: ['static/js/**/*.js']
};

gulp.task('default', ['sass', 'scripts']);
gulp.task('sass', function (done) {
    gulp.src('static/scss/**/*.scss')
        .pipe(sass())
        .on('error', sass.logError)
        .pipe(gulp.dest('static/dist/css/'))
        .pipe(minifyCss({
            keepSpecialComments: 0
        }))
        .pipe(rename({extname: '.min.css'}))
        .pipe(gulp.dest('static/dist/css/'))
        .on('end', done);
});

gulp.task('scripts', function () {
    return gulp.src(['static/js/**/*.js'])
        .pipe(concat('app.js'))
        .pipe(gulp.dest('dist/js/'))
        .pipe(rename({extname: '.min.js'}))
        //.pipe(uglify({
        //    mangle: false,
        //    output: {
        //        beautify: true
        //    }}))
        .pipe(gulp.dest('dist/js/'));
});
gulp.task('watch', function () {
    gulp.watch(paths.sass, ['sass']);
});
gulp.task('jswatch', function () {
    gulp.watch(paths.scripts, ['scripts']);
});

/*gulp.task('install', ['git-check'], function() {
 return bower.commands.install()
 .on('log', function(data) {
 gutil.log('bower', gutil.colors.cyan(data.id), data.message);
 });
 });

 gulp.task('git-check', function(done) {
 if (!sh.which('git')) {
 console.log(
 '  ' + gutil.colors.red('Git is not installed.'),
 '\n  Git, the version control system, is required to download Ionic.',
 '\n  Download git here:', gutil.colors.cyan('http://git-scm.com/downloads') + '.',
 '\n  Once git is installed, run \'' + gutil.colors.cyan('gulp install') + '\' again.'
 );
 process.exit(1);
 }
 done();
 });*/
