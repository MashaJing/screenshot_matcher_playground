# Screenshot Matcher playground
Easy example for getting started with Matchu Piccu plugin.

Project contains 2 branches:
- master
- branch-with-picture-changes

The golden version of the app is available here: https://mashajing.github.io/screenshot_matcher_playground/
We will run scenario locally on `branch-with-picture-changes`.

## Local run
1. Install all the necessary dependencies:
```
make install-dependencies
```
2. Start the server
```
make up
```
3. Run the test
```
make e2e
```
The test will fail as we've made some changes in `branch-with-picture-changes`.

4. Check the results. New folder `snapshots/` should appear, there you will find 2 screenshots:
- expected result
- comparison between the screenshots taken
