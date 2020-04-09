# Telestream Cloud Quality Control Python SDK

This library provides a low-level interface to the REST API of Telestream Cloud, the online video encoding service.

## Requirements.

Python 2.7 and 3.4+

## Getting Started
### Create new project and submit job

```python
# Create new project based on DPP V5 IMX template
project = client.create_project(options = {"template" : "dpp_v5_imx",
                                           "name" : "SampleProject" })

# Start new job and override some tests
client.create_job(project = project.id, data = {"url" : "https://samples.ffmpeg.org/mov/mp4/panda.mp4"
                                                "options" : {"file_tests" : {
                                                    "container_test" : {
                                                        "conatiner" : "Mp4",
                                                        "reject_on_error" : True},
                                                    "video_codec_test" : {
                                                        "video_codec" : "H264",
                                                        "video_profile" : "H264Main",
                                                        }
                                                }}
})
```


```python
# Create new project based on DPP V5 IMX template
project = client.create_project(options = {"template" : "dpp_v5_imx",
                                           "name" : "SampleProject" })

# Start new job with default template attributes
client.create_job(project = project.id, data = {"url" : "https://samples.ffmpeg.org/mov/mp4/panda.mp4"})
```

```python
# Create new project based on DPP V5 IMX template
project = client.create_project(options = {"template" : "ard_zdf_1_a",
                                           "name" : "SampleProject"})

# Start new job with PSE check enabled
client.create_job(project = project.id, data = {"url" : "https://samples.ffmpeg.org/mov/mp4/panda.mp4"
                                                "options" : {"video_tests" : {
                                                    "video_test" : [{
                                                        "flash_test":
                                                        {"checked": True,
                                                         "check_type" : "PSEStandard",
                                                         "check_for_extended": True,
                                                         "check_for_red": True,
                                                         "check_for_patterns": True,
                                                         "reject_on_error": True,
                                                         "do_correction": False}
                                                    }]
                                                }
                                                }
})
```

### Upload file to QC service

```python
import telestream_cloud_qc as qc

api_key = 'tcs_xxx'
project = 'tg01xxxxxxxxxxxx'
filepath = "/tmp/video.mp4"

client = qc.QcApi()
client.api_client.configuration.api_key['X-Api-Key'] = api_key

upload = qc.Uploader(project, client, filepath, profiles)
upload.setup()
video_id = upload.start()
```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloud.telestream.net/qc/v1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*QcApi* | [**cancel_job**](docs/QcApi.md#cancel_job) | **PUT** /projects/{project_id}/jobs/{job_id}/cancel.json | Cancel QC job
*QcApi* | [**create_job**](docs/QcApi.md#create_job) | **POST** /projects/{project_id}/jobs.json | Create a new job
*QcApi* | [**create_project**](docs/QcApi.md#create_project) | **POST** /projects.json | Create a new project
*QcApi* | [**get_job**](docs/QcApi.md#get_job) | **GET** /projects/{project_id}/jobs/{job_id}.json | Get QC job
*QcApi* | [**get_project**](docs/QcApi.md#get_project) | **GET** /projects/{project_id}.json | Get project by Id
*QcApi* | [**import_template**](docs/QcApi.md#import_template) | **POST** /projects/import.json | Import Vidchecker template
*QcApi* | [**list_jobs**](docs/QcApi.md#list_jobs) | **GET** /projects/{project_id}/jobs.json | Get jobs form projects
*QcApi* | [**list_projects**](docs/QcApi.md#list_projects) | **GET** /projects.json | List all projects for an account
*QcApi* | [**modify_project**](docs/QcApi.md#modify_project) | **PUT** /projects/{project_id}.json | Modify project
*QcApi* | [**proxy**](docs/QcApi.md#proxy) | **GET** /projects/{project_id}/jobs/{job_id}/proxy.json | 
*QcApi* | [**remove_job**](docs/QcApi.md#remove_job) | **DELETE** /projects/{project_id}/jobs/{job_id}.json | Remove QC job
*QcApi* | [**remove_project**](docs/QcApi.md#remove_project) | **DELETE** /projects/{project_id}.json | Remove project
*QcApi* | [**signed_urls**](docs/QcApi.md#signed_urls) | **GET** /projects/{project_id}/jobs/{job_id}/signed-urls.json | Get QC job signed urls
*QcApi* | [**templates**](docs/QcApi.md#templates) | **GET** /templates.json | List all templates


## Documentation For Models

 - [ActiveFormatDescriptorTest](docs/ActiveFormatDescriptorTest.md)
 - [ActiveFormatTest](docs/ActiveFormatTest.md)
 - [AdvancedGopLengthTest](docs/AdvancedGopLengthTest.md)
 - [Alert](docs/Alert.md)
 - [ArrayOfPictureEssenceCoding](docs/ArrayOfPictureEssenceCoding.md)
 - [ArrayOfSoundEssenceCoding](docs/ArrayOfSoundEssenceCoding.md)
 - [As11Rules](docs/As11Rules.md)
 - [As11UkDppMetadataTest](docs/As11UkDppMetadataTest.md)
 - [As11XprofileTest](docs/As11XprofileTest.md)
 - [AudioBitDepthTest](docs/AudioBitDepthTest.md)
 - [AudioBitrateTest](docs/AudioBitrateTest.md)
 - [AudioChannelPositionsTest](docs/AudioChannelPositionsTest.md)
 - [AudioChannelsTest](docs/AudioChannelsTest.md)
 - [AudioClippingTest](docs/AudioClippingTest.md)
 - [AudioCodecTest](docs/AudioCodecTest.md)
 - [AudioCodecType](docs/AudioCodecType.md)
 - [AudioConfig](docs/AudioConfig.md)
 - [AudioConfigs](docs/AudioConfigs.md)
 - [AudioDialnormTest](docs/AudioDialnormTest.md)
 - [AudioFrequencyTest](docs/AudioFrequencyTest.md)
 - [AudioLengthTest](docs/AudioLengthTest.md)
 - [AudioLoudnessItest](docs/AudioLoudnessItest.md)
 - [AudioLoudnessMtest](docs/AudioLoudnessMtest.md)
 - [AudioLoudnessRangeTest](docs/AudioLoudnessRangeTest.md)
 - [AudioLoudnessStest](docs/AudioLoudnessStest.md)
 - [AudioMinLevelDurationTest](docs/AudioMinLevelDurationTest.md)
 - [AudioPeakLevelTest](docs/AudioPeakLevelTest.md)
 - [AudioPhaseTest](docs/AudioPhaseTest.md)
 - [AudioPpmLevelTest](docs/AudioPpmLevelTest.md)
 - [AudioSampleRateTest](docs/AudioSampleRateTest.md)
 - [AudioStream](docs/AudioStream.md)
 - [AudioTracksTest](docs/AudioTracksTest.md)
 - [AudioTransientTest](docs/AudioTransientTest.md)
 - [AvcCodedContentKindTest](docs/AvcCodedContentKindTest.md)
 - [AvcContentKind](docs/AvcContentKind.md)
 - [AvcSpsPpsTest](docs/AvcSpsPpsTest.md)
 - [BitRateMode](docs/BitRateMode.md)
 - [BitRateModeTest](docs/BitRateModeTest.md)
 - [BlackFrameTest](docs/BlackFrameTest.md)
 - [BlackLevelTest](docs/BlackLevelTest.md)
 - [BlankingTest](docs/BlankingTest.md)
 - [BlockinessTest](docs/BlockinessTest.md)
 - [BoolValueTest](docs/BoolValueTest.md)
 - [BufferSizeTest](docs/BufferSizeTest.md)
 - [CabacTest](docs/CabacTest.md)
 - [CadenceTest](docs/CadenceTest.md)
 - [CadenceType](docs/CadenceType.md)
 - [CaptionsTest](docs/CaptionsTest.md)
 - [ChanPos](docs/ChanPos.md)
 - [ChanPositions](docs/ChanPositions.md)
 - [Channels](docs/Channels.md)
 - [ChromaLevelTest](docs/ChromaLevelTest.md)
 - [ChromaSubsampling](docs/ChromaSubsampling.md)
 - [ChromaSubsamplingTest](docs/ChromaSubsamplingTest.md)
 - [CleanApertureTest](docs/CleanApertureTest.md)
 - [ColorBarStandardType](docs/ColorBarStandardType.md)
 - [ColorRangeTest](docs/ColorRangeTest.md)
 - [ColorSitingTest](docs/ColorSitingTest.md)
 - [ColorSpaceType](docs/ColorSpaceType.md)
 - [ColourBarsTest](docs/ColourBarsTest.md)
 - [ComponentDepthTest](docs/ComponentDepthTest.md)
 - [Container](docs/Container.md)
 - [ContainerEssenceConsistencyTest](docs/ContainerEssenceConsistencyTest.md)
 - [ContainerTest](docs/ContainerTest.md)
 - [ContainerType](docs/ContainerType.md)
 - [CorruptFrameTest](docs/CorruptFrameTest.md)
 - [DefaultOrCustomType](docs/DefaultOrCustomType.md)
 - [DigitalDropoutTest](docs/DigitalDropoutTest.md)
 - [DigitalSilenceAtStartEndTest](docs/DigitalSilenceAtStartEndTest.md)
 - [DigitalSilenceWholeTrackTest](docs/DigitalSilenceWholeTrackTest.md)
 - [DontCopyAvDelayTest](docs/DontCopyAvDelayTest.md)
 - [DropFrameTest](docs/DropFrameTest.md)
 - [DropFrameType](docs/DropFrameType.md)
 - [DropoutTest](docs/DropoutTest.md)
 - [EmbeddedXmlDocuments](docs/EmbeddedXmlDocuments.md)
 - [EnhancedSyntaxTest](docs/EnhancedSyntaxTest.md)
 - [ExtendedBool](docs/ExtendedBool.md)
 - [ExtendedBoolValueTest](docs/ExtendedBoolValueTest.md)
 - [ExtraAudioLayoutModes](docs/ExtraAudioLayoutModes.md)
 - [FieldDominanceTest](docs/FieldDominanceTest.md)
 - [FieldOrderTest](docs/FieldOrderTest.md)
 - [FieldOrderType](docs/FieldOrderType.md)
 - [FileBitrateTest](docs/FileBitrateTest.md)
 - [FileConfig](docs/FileConfig.md)
 - [FileDurationTest](docs/FileDurationTest.md)
 - [FileFormatSpecificationIdentificationLabel](docs/FileFormatSpecificationIdentificationLabel.md)
 - [FlashTest](docs/FlashTest.md)
 - [ForceColorSpaceTest](docs/ForceColorSpaceTest.md)
 - [FrameAspectRatioTest](docs/FrameAspectRatioTest.md)
 - [FramerateTest](docs/FramerateTest.md)
 - [FramesizeTest](docs/FramesizeTest.md)
 - [FreezeFrameTest](docs/FreezeFrameTest.md)
 - [GopLengthTest](docs/GopLengthTest.md)
 - [GopOrder](docs/GopOrder.md)
 - [GopReport](docs/GopReport.md)
 - [HdrStandardType](docs/HdrStandardType.md)
 - [HdrTest](docs/HdrTest.md)
 - [HeaderByteCountTest](docs/HeaderByteCountTest.md)
 - [HeaderFillTest](docs/HeaderFillTest.md)
 - [ITunesCompatibilityTest](docs/ITunesCompatibilityTest.md)
 - [IgnoreVbiTest](docs/IgnoreVbiTest.md)
 - [ImfConformanceTest](docs/ImfConformanceTest.md)
 - [IndexTableTest](docs/IndexTableTest.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Job](docs/Job.md)
 - [JobData](docs/JobData.md)
 - [JobsCollection](docs/JobsCollection.md)
 - [KagSizeTest](docs/KagSizeTest.md)
 - [LayoutTest](docs/LayoutTest.md)
 - [LayoutType](docs/LayoutType.md)
 - [LetterboxingTest](docs/LetterboxingTest.md)
 - [LocationTest](docs/LocationTest.md)
 - [LongMinMaxTest](docs/LongMinMaxTest.md)
 - [LongValueTest](docs/LongValueTest.md)
 - [LossOfChromaTest](docs/LossOfChromaTest.md)
 - [LoudnessMode](docs/LoudnessMode.md)
 - [LowPassFilterType](docs/LowPassFilterType.md)
 - [MbaffTest](docs/MbaffTest.md)
 - [Media](docs/Media.md)
 - [MediaOfflineTest](docs/MediaOfflineTest.md)
 - [ModifyProjectBody](docs/ModifyProjectBody.md)
 - [ModifyVidChecker8Body](docs/ModifyVidChecker8Body.md)
 - [MustOrMustNot](docs/MustOrMustNot.md)
 - [MxfColorSiting](docs/MxfColorSiting.md)
 - [MxfFieldDominance](docs/MxfFieldDominance.md)
 - [MxfKeyTest](docs/MxfKeyTest.md)
 - [MxfOpTest](docs/MxfOpTest.md)
 - [MxfTest](docs/MxfTest.md)
 - [MxfVersion](docs/MxfVersion.md)
 - [NetflixPhotonTest](docs/NetflixPhotonTest.md)
 - [NielsenWatermarkDetectionTest](docs/NielsenWatermarkDetectionTest.md)
 - [OpenOrClosed](docs/OpenOrClosed.md)
 - [OperationalPattern](docs/OperationalPattern.md)
 - [OperationalPatternTest](docs/OperationalPatternTest.md)
 - [OptionalFlag](docs/OptionalFlag.md)
 - [PSeParameterType](docs/PSeParameterType.md)
 - [PaddingBitsTest](docs/PaddingBitsTest.md)
 - [PartitionStatusTest](docs/PartitionStatusTest.md)
 - [PicFrameSizeTest](docs/PicFrameSizeTest.md)
 - [PictureEssenceCoding](docs/PictureEssenceCoding.md)
 - [PictureEssenceCodingTest](docs/PictureEssenceCodingTest.md)
 - [PictureEssenceConstraints](docs/PictureEssenceConstraints.md)
 - [PictureOffsetsTest](docs/PictureOffsetsTest.md)
 - [PixelAspectRatioTest](docs/PixelAspectRatioTest.md)
 - [PpmMode](docs/PpmMode.md)
 - [Project](docs/Project.md)
 - [ProjectBody](docs/ProjectBody.md)
 - [Proxy](docs/Proxy.md)
 - [RatioOrLinesType](docs/RatioOrLinesType.md)
 - [RatioTest](docs/RatioTest.md)
 - [ReferenceLevelsTest](docs/ReferenceLevelsTest.md)
 - [RequireOrDisallow](docs/RequireOrDisallow.md)
 - [RgbGamutTest](docs/RgbGamutTest.md)
 - [RipPresentTest](docs/RipPresentTest.md)
 - [RunInTest](docs/RunInTest.md)
 - [SdtiTimecodeContinuityTest](docs/SdtiTimecodeContinuityTest.md)
 - [SecsOrFramesType](docs/SecsOrFramesType.md)
 - [SensitivityType](docs/SensitivityType.md)
 - [SidsAnyOrSpecific](docs/SidsAnyOrSpecific.md)
 - [SignalStandardTest](docs/SignalStandardTest.md)
 - [SingleColorTest](docs/SingleColorTest.md)
 - [SingleSampleDescriptionTest](docs/SingleSampleDescriptionTest.md)
 - [SoundEssenceCoding](docs/SoundEssenceCoding.md)
 - [SoundEssenceCodingTest](docs/SoundEssenceCodingTest.md)
 - [SpsPpsTest](docs/SpsPpsTest.md)
 - [StartTcRangeMethod](docs/StartTcRangeMethod.md)
 - [StartTimecodeTest](docs/StartTimecodeTest.md)
 - [StripeTest](docs/StripeTest.md)
 - [SubsamplingTest](docs/SubsamplingTest.md)
 - [Summary](docs/Summary.md)
 - [SynchronizationEvent](docs/SynchronizationEvent.md)
 - [TeletextType](docs/TeletextType.md)
 - [Template](docs/Template.md)
 - [TextStreamTest](docs/TextStreamTest.md)
 - [TimeCodeSource](docs/TimeCodeSource.md)
 - [TimecodeContinuityTest](docs/TimecodeContinuityTest.md)
 - [TimecodeTrackTest](docs/TimecodeTrackTest.md)
 - [ToneType](docs/ToneType.md)
 - [TrackIdTest](docs/TrackIdTest.md)
 - [TrackSelectTest](docs/TrackSelectTest.md)
 - [TrackSelectorType](docs/TrackSelectorType.md)
 - [UkDppShim](docs/UkDppShim.md)
 - [UseStartTimecodeTest](docs/UseStartTimecodeTest.md)
 - [VersionTest](docs/VersionTest.md)
 - [VidChecker8Body](docs/VidChecker8Body.md)
 - [VidChecker8JobData](docs/VidChecker8JobData.md)
 - [Vidchecker8](docs/Vidchecker8.md)
 - [VideoBitDepthTest](docs/VideoBitDepthTest.md)
 - [VideoBitrateTest](docs/VideoBitrateTest.md)
 - [VideoCodecTest](docs/VideoCodecTest.md)
 - [VideoCodecType](docs/VideoCodecType.md)
 - [VideoConfig](docs/VideoConfig.md)
 - [VideoConfigs](docs/VideoConfigs.md)
 - [VideoDescriptorTest](docs/VideoDescriptorTest.md)
 - [VideoDescriptorType](docs/VideoDescriptorType.md)
 - [VideoLevelType](docs/VideoLevelType.md)
 - [VideoLineMapTest](docs/VideoLineMapTest.md)
 - [VideoProfileType](docs/VideoProfileType.md)
 - [VideoSegmentDetectionTest](docs/VideoSegmentDetectionTest.md)
 - [VideoStream](docs/VideoStream.md)
 - [VideoSubDescriptorTest](docs/VideoSubDescriptorTest.md)
 - [VideoSubDescriptorType](docs/VideoSubDescriptorType.md)
 - [WrappingType](docs/WrappingType.md)
 - [WrappingTypeTest](docs/WrappingTypeTest.md)


## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header


## Author

cloudsupport@telestream.net


